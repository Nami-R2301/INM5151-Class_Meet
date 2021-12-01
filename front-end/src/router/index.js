import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/Home.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/Connexion.vue')
  },
  {
    path: '/forum/:category',
    name: 'Forum',
    component: () => import('../views/Forum.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  routes
})

export default router
