/**
 * Script to update all hardcoded API URLs to use getApiUrl helper
 * Run this script after creating the api.ts utility
 */

const fs = require('fs');
const path = require('path');

const srcDir = path.join(__dirname, 'src');
const filesToUpdate = [];

// Find all .vue and .ts files
function findFiles(dir) {
  const files = fs.readdirSync(dir);
  files.forEach(file => {
    const filePath = path.join(dir, file);
    const stat = fs.statSync(filePath);
    if (stat.isDirectory() && file !== 'node_modules') {
      findFiles(filePath);
    } else if (file.endsWith('.vue') || file.endsWith('.ts')) {
      filesToUpdate.push(filePath);
    }
  });
}

findFiles(srcDir);

let updatedCount = 0;

filesToUpdate.forEach(filePath => {
  let content = fs.readFileSync(filePath, 'utf8');
  let modified = false;
  
  // Skip if already using getApiUrl
  if (content.includes('getApiUrl') || content.includes('apiFetch')) {
    return;
  }
  
  // Pattern 1: fetch('https://api.irpps.org/api/...')
  const pattern1 = /fetch\(['"]https:\/\/api\.irpps\.org(\/api\/[^'"]+)['"]/g;
  if (pattern1.test(content)) {
    content = content.replace(pattern1, (match, endpoint) => {
      modified = true;
      return `fetch(getApiUrl('${endpoint}')`;
    });
  }
  
  // Pattern 2: `https://api.irpps.org${...}`
  const pattern2 = /`https:\/\/api\.irpps\.org\$\{([^}]+)\}`/g;
  if (pattern2.test(content)) {
    content = content.replace(pattern2, (match, expr) => {
      modified = true;
      return `getApiUrl(\`${expr}\`)`;
    });
  }
  
  // Pattern 3: 'https://api.irpps.org' + ...
  const pattern3 = /['"]https:\/\/api\.irpps\.org['"]\s*\+/g;
  if (pattern3.test(content)) {
    // This is more complex, need to handle manually
    console.log(`⚠️  Manual update needed for: ${filePath}`);
  }
  
  if (modified) {
    // Add import if not present
    if (!content.includes("import { getApiUrl }")) {
      const importLine = content.includes("from '@/utils/assets'") 
        ? "import { getApiUrl } from '@/utils/api';"
        : "import { getApiUrl } from '@/utils/api';\n";
      
      // Find the last import statement
      const importMatch = content.match(/(import\s+.*?from\s+['"].*?['"];?\n?)+/);
      if (importMatch) {
        const lastImportIndex = importMatch[0].lastIndexOf('import');
        const insertIndex = importMatch.index + importMatch[0].length;
        content = content.slice(0, insertIndex) + '\n' + importLine + content.slice(insertIndex);
      } else {
        // Add at the beginning of script section
        const scriptMatch = content.match(/<script[^>]*>/);
        if (scriptMatch) {
          content = content.slice(0, scriptMatch.index + scriptMatch[0].length) + 
                   '\n' + importLine + 
                   content.slice(scriptMatch.index + scriptMatch[0].length);
        }
      }
    }
    
    fs.writeFileSync(filePath, content, 'utf8');
    updatedCount++;
    console.log(`✅ Updated: ${path.relative(srcDir, filePath)}`);
  }
});

console.log(`\n✨ Updated ${updatedCount} files`);

