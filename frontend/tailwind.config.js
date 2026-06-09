/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html', './src/**/*.{js,jsx}'],
  theme: {
    extend: {
      fontFamily: {
        display: ['"Space Grotesk"', 'sans-serif'],
        body: ['"Sora"', 'sans-serif'],
      },
      colors: {
        ink: {
          950: '#06101c',
          900: '#0b1726',
          800: '#122033',
        },
        sand: {
          50: '#fefbf3',
          100: '#f8f1dd',
          200: '#f1deaa',
        },
        accent: {
          500: '#f59e0b',
          600: '#d97706',
        },
      },
      boxShadow: {
        glow: '0 0 0 1px rgba(245,158,11,0.18), 0 30px 80px rgba(8,15,26,0.45)',
      },
      backgroundImage: {
        'aurora-grid': 'radial-gradient(circle at top left, rgba(56,189,248,0.22), transparent 30%), radial-gradient(circle at top right, rgba(245,158,11,0.24), transparent 26%), linear-gradient(180deg, rgba(6,16,28,0.98), rgba(9,20,36,1))',
      },
    },
  },
  plugins: [],
}
