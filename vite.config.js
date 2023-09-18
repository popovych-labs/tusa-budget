import { defineConfig } from 'vite';

export default {
    root: "./frontend",
    build: {
        // watch: './frontnend',
        emptyOutDir: true,
        minify: false,
        outDir: "../backend/src/dist"
    }
}