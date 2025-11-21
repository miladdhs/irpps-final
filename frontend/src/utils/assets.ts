/**
 * Get static asset URL
 * In development (Vite), uses /img/...
 * In production (Django), uses /assets/img/...
 */
export function getAssetUrl(path: string): string {
  // Remove leading slash if present
  const cleanPath = path.startsWith('/') ? path.slice(1) : path;
  
  // In production or if we're served by Django, use /assets/
  // Check if we're in production mode
  if (import.meta.env.PROD) {
    // In production, Django serves static files from /assets/
    return `/assets/${cleanPath}`;
  }
  
  // In development, Vite serves files from public/ directory at root
  return `/${cleanPath}`;
}





