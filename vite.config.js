import { defineConfig } from 'vite';

export default {
    root: "./frontend",
    build: {
        watch: './frontned',
        emptyOutDir: true,
        minify: false,
        outDir: "../backend/src/dist"
    }
}