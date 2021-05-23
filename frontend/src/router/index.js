import Vue from 'vue'
import VueRouter from 'vue-router'
import BooksList from '../views/BooksList.vue'
import AuthorsList from '../views/AuthorsList'
import ReadersList from '../views/ReadersList'

Vue.use(VueRouter)

const routes = [
  {
    path: '/books',
    name: 'books',
    component: BooksList
  },
  {
    path: '/authors',
    name: 'authors',
    component: AuthorsList
  },
  {
    path: '/readers',
    name: 'readers',
    component: ReadersList
  },
]

const router = new VueRouter({
    routes,
    mode: 'history'
})

export default router
