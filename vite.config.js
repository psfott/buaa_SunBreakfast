import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

import AutoImport from 'unplugin-auto-import/vite'
import Components from 'unplugin-vue-components/vite'
import { ElementPlusResolver } from 'unplugin-vue-components/resolvers'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [
    vue(),
    // ...
    AutoImport({
      resolvers: [ElementPlusResolver()],
    }),
    Components({
      resolvers: [
        // 1. 配置elementPlus采用sass样式配色系统
        //ElementPlusResolver({ importStyle: "sass" }),
        [ElementPlusResolver()],
      ],
    }),
  ],
  server: {
    host: '127.0.0.1',
    port: 8001,
    cors: true,
    open: true,
    proxy:{
      '/api': {
        target:'http://127.0.0.1:8000',
        // target: 'http://127.0.0.1:4523/m1/3177387-0-default',
        // target:'http://8.130.107.193',
        changeOrigin: true,
        rewrite: path => path.replace(/^\/api/, '')
      }

    }
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
