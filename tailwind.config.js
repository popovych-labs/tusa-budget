/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    ".\\backend\\src\\templates\\*.html",
    ".\\frontend\\**\\*.js"
  ],
  theme: {
    extend: {},
  },
  plugins: [
    'prettier-plugin-tailwindcss'
  ],
}

