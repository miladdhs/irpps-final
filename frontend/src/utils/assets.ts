/**
 * Get static asset URL
 * In both development and production, uses /img/... (root path)
 * Files in public/ folder are served directly from root by nginx
 */
export function getAssetUrl(path: string): string {
  // Remove leading slash if present
  const cleanPath = path.startsWith('/') ? path.slice(1) : path;
  
  // Always use root path - nginx serves public/ files from root
  return `/${cleanPath}`;
}





