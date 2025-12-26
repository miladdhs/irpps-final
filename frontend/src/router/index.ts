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
  { path: '/about/history', name: 'history', component: () => import('../views/History.vue') },
  { path: '/about/gallery', name: 'gallery', component: () => import('../views/Gallery.vue') },
  { path: '/about/board-first', name: 'board-first', component: () => import('../views/BoardFirst.vue') },
  { path: '/about/board-second', name: 'board-second', component: () => import('../views/BoardSecond.vue') },
  { path: '/about/board-third', name: 'board-third', component: () => import('../views/BoardThird.vue') },
  { path: '/services', name: 'services', component: Services },
  { path: '/news', name: 'news', component: () => import('../views/News.vue') },
  { path: '/events', name: 'events', component: () => import('../views/Events.vue') },
  { path: '/team', name: 'team', component: Team },
  { path: '/contact', name: 'contact', component: Contact },
  { path: '/register', name: 'register', component: Register },
  { path: '/education', name: 'education', component: () => import('../views/Education.vue') },
  { path: '/publications', name: 'publications', component: () => import('../views/Publications.vue') },
  { path: '/associations', name: 'associations', component: () => import('../views/Associations.vue') },
  { path: '/advertising', name: 'advertising', component: () => import('../views/Advertising.vue') },
  { path: '/doctors', name: 'doctors', component: () => import('../views/Doctors.vue') },
  { path: '/news/:slug', name: 'news-detail', component: () => import('../views/NewsDetail.vue') },
  { path: '/events/:slug', name: 'event-detail', component: () => import('../views/EventDetail.vue') },
  { path: '/dashboard', name: 'dashboard', component: () => import('../views/Dashboard.vue') }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;


