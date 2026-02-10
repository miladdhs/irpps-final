/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        'primary': '#137fec',
        'background-light': '#f6f7f8',
        'background-dark': '#101922',
      },
      fontFamily: {
        'display': ['Vazirmatn', 'Tahoma', 'sans-serif'],
        'sans': ['Vazirmatn', 'Tahoma', 'sans-serif'],
      },
      borderRadius: {
        'DEFAULT': '0.25rem',
        'lg': '0.5rem',
        'xl': '0.75rem',
        'full': '9999px',
      },
    },
  },
  plugins: [],
}
