const { Container } = require('postcss')

/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./me/templates/**/*.html",
    "./myweb/templates/**/*.html",
  ],
  theme: {
    extend: { extend: {} },
  },
  plugins: [],
}

tailwind.config = {
  prefix: 'tw-',
  corePlugins: {
    preflight: false,
    container: false,
  },
}