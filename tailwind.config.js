const { Container } = require('postcss')

/** @type {import('tailwindcss').Config} */
module.exports = {
  prefix: 'tw-',
  corePlugins: {
    preflight: false,
    container: false,
  },
  content: [
    "./me/templates/**/*.html",
    "./myweb/templates/**/*.html",
  ],
  theme: {
    extend: { extend: {} },
  },
  plugins: [],  
}
