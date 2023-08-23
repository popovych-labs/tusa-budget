/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    ".\\backend\\src\\templates\\*.html",
    ".\\backend\\src\\js\\*.js"
  ],
  theme: {
    extend: {},
  },
  plugins: [
    require('@tailwindcss/forms')
  ],
}

