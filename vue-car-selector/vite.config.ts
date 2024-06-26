import {defineConfig} from 'vite'
import { fileURLToPath, URL } from "url";
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
    plugins: [vue()],
    resolve: {
        extensions: ["*", ".js", ".ts", ".vue", ".json"],
        alias: {
            "@": fileURLToPath(new URL("./src", import.meta.url)),
        },
    },
    css: {
        preprocessorOptions: {
            less: {
                modifyVars: {
                },
                javascriptEnabled: true,
            },
        },
    },
})
