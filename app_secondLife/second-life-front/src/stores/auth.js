// stores/auth.js
import { defineStore } from 'pinia'

export const useAuthStore = defineStore('auth', {
  state: () => ({
    isLoggedIn: !!localStorage.getItem('access_token'),
    user: null,
  }),
  actions: {
    setUser(user) {
      this.user = user
      this.isLoggedIn = true
    },
    logout() {
      localStorage.removeItem('access_token')
      localStorage.removeItem('refresh_token')
      this.user = null
      this.isLoggedIn = false
    },
    checkAuth() {
      const token = localStorage.getItem('access_token')
      if (!token) {
        this.logout()
      }
    },
  },
})
