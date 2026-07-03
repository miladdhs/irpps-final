import { getApiUrl } from './api';

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

export const DEFAULT_NEWS_IMAGE = '/img/news.png';
export const DEFAULT_EVENT_IMAGE = '/img/events.png';

export function resolveImageUrl(value: string | null | undefined, fallback: string): string {
  const image = String(value || '').trim();

  if (!image || image === 'null' || image === 'undefined') {
    return fallback;
  }

  if (image.startsWith('http://') || image.startsWith('https://') || image.startsWith('data:')) {
    return image;
  }

  if (image.startsWith('/media/')) {
    return getApiUrl(image);
  }

  if (image.startsWith('/')) {
    return image;
  }

  if (image.startsWith('media/')) {
    return getApiUrl(`/${image}`);
  }

  return `/${image}`;
}





