import { fileURLToPath, URL } from "node:url";
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import vueDevTools from "vite-plugin-vue-devtools";

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue(), vueDevTools()],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
  server: {
    host: "localhost", // Use '0.0.0.0' to allow access from external devices
    port: 8000, // Change this to your desired port
  },
  test: {
    globals: true,
    environment: "jsdom",
    setupFiles: "./test/setup.js", // Add this line
  },
});
