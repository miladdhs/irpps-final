import { createRouter, createWebHistory } from 'vue-router';
import Home from '../views/Home.vue';
import About from '../views/About.vue';
import Services from '../views/Services.vue';
import Team from '../views/Team.vue';
import Contact from '../views/Contact.vue';
import Register from '../views/Register.vue';

const routes = [
  { path: '/', name: 'home', component: Home },
  { path: '/about', name: 'about', component: About },
  { path: '/services', name: 'services', component: Services },
  { path: '/team', name: 'team', component: Team },
  { path: '/contact', name: 'contact', component: Contact },
  { path: '/register', name: 'register', component: Register },
  { path: '/news/:slug', name: 'news-detail', component: () => import('../views/NewsDetail.vue') },
  { path: '/events/:slug', name: 'event-detail', component: () => import('../views/EventDetail.vue') },
  { path: '/dashboard', name: 'dashboard', component: () => import('../views/Dashboard.vue') }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;


