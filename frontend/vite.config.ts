import { defineConfig } from 'vite';
import vue from '@vitejs/plugin-vue';
import { resolve } from 'path';

export default defineConfig({
  plugins: [vue()],
  server: {
    port: 5173,
    host: true,
    fs: {
      // Allow serving files from one level up to the project root
      allow: ['..'],
      strict: false
    },
    proxy: {
      '/api': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        secure: false,
      },
      '/static': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        secure: false,
      },
      '/media': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        secure: false,
      },
      '/assets': {
        target: 'http://localhost:8000',
        changeOrigin: true,
        secure: false,
      }
    },
    // Ignore templates directory and other problematic paths
    watch: {
      ignored: ['**/templates/**', '**/node_modules/**', '**/.git/**', '**/data/**']
    }
  },
  build: {
    sourcemap: false,
    outDir: 'dist',
    rollupOptions: {
      input: {
        main: resolve(__dirname, 'index.html')
      }
    }
  },
  css: {
    devSourcemap: false,
    preprocessorOptions: {
      scss: {
        silenceDeprecations: ['legacy-js-api', 'import', 'global-builtin', 'color-functions', 'slash-div']
      }
    }
  },
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src')
    }
  },
  publicDir: 'public',
  base: '/',
  assetsInclude: ['**/*.jpg', '**/*.png', '**/*.svg', '**/*.woff', '**/*.woff2', '**/*.ttf', '**/*.eot'],
  optimizeDeps: {
    exclude: []
  }
});
