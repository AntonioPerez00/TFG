/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        fondo: '#FFFDF8',
        borde: '#f1e2bc',
      },
    },
  },
  plugins: [],
}
