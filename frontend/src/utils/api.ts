/**
 * API Configuration
 * Handles API base URL for both development and production environments
 */

// Determine API base URL based on environment
export const getApiBaseUrl = (): string => {
  // In development, use relative path (Vite proxy will handle it)
  // @ts-ignore - Vite provides import.meta.env
  if (import.meta.env.DEV) {
    return '';
  }
  
  // In production, use the production API URL
  // This can be overridden by environment variable if needed
  // @ts-ignore - Vite provides import.meta.env
  return import.meta.env.VITE_API_BASE_URL || 'https://api.irpps.org';
};

/**
 * Get full API URL for an endpoint
 * @param endpoint - API endpoint (e.g., '/api/accounts/login/')
 * @returns Full API URL
 */
export const getApiUrl = (endpoint: string): string => {
  const baseUrl = getApiBaseUrl();
  const cleanEndpoint = endpoint.startsWith('/') ? endpoint : `/${endpoint}`;
  return `${baseUrl}${cleanEndpoint}`;
};

/**
 * Helper function for fetch API calls with proper configuration
 */
export const apiFetch = async (
  endpoint: string,
  options: RequestInit = {}
): Promise<Response> => {
  const url = getApiUrl(endpoint);
  
  const defaultOptions: RequestInit = {
    credentials: 'include',
    headers: {
      'Content-Type': 'application/json',
      ...options.headers,
    },
  };
  
  return fetch(url, { ...defaultOptions, ...options });
};

