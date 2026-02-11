import { createRouter, createWebHistory } from 'vue-router';
import { useAuthStore } from '@/stores/auth';
import Home from '../views/Home.vue';
import About from '../views/About.vue';
import Services from '../views/Services.vue';
import Team from '../views/Team.vue';
import Contact from '../views/Contact.vue';

const routes = [
  { path: '/', name: 'home', component: Home },
  { path: '/about', name: 'about', component: About },
  { path: '/about/history', name: 'history', component: () => import('../views/History.vue') },
  { path: '/about/gallery', name: 'gallery', component: () => import('../views/Gallery.vue') },
  { path: '/about/board-members', name: 'board-members', component: () => import('../views/BoardMembers.vue') },
  // Legacy routes - redirect to new board members page
  { path: '/about/board-first', redirect: '/about/board-members' },
  { path: '/about/board-second', redirect: '/about/board-members' },
  { path: '/about/board-third', redirect: '/about/board-members' },
  { path: '/services', name: 'services', component: Services },
  { path: '/news', name: 'news', component: () => import('../views/News.vue') },
  { path: '/events', name: 'events', component: () => import('../views/Events.vue') },
  { path: '/team', name: 'team', component: Team },
  { path: '/contact', name: 'contact', component: Contact },
  
  // Auth routes
  { path: '/login', name: 'login', component: () => import('../views/Login.vue'), meta: { guest: true } },
  { path: '/register', name: 'register', component: () => import('../views/Register.vue'), meta: { guest: true } },
  
  // Education & Publications
  { path: '/education', name: 'education', component: () => import('../views/Education.vue') },
  { path: '/education/doctors', name: 'doctors', component: () => import('../views/Doctors.vue') },
  { path: '/doctors', redirect: '/education/doctors' },
  { path: '/publications', name: 'publications', component: () => import('../views/Publications.vue') },
  { path: '/associations', name: 'associations', component: () => import('../views/Associations.vue') },
  { path: '/advertising', name: 'advertising', component: () => import('../views/Advertising.vue') },
  
  // Detail pages
  { path: '/news/:slug', name: 'news-detail', component: () => import('../views/NewsDetail.vue') },
  { path: '/events/:slug', name: 'event-detail', component: () => import('../views/EventDetail.vue') },
  
  // Protected routes (require authentication)
  { 
    path: '/dashboard', 
    name: 'dashboard', 
    component: () => import('../views/Dashboard.vue'),
    meta: { requiresAuth: true }
  },
  { 
    path: '/profile', 
    name: 'profile', 
    component: () => import('../views/Profile.vue'),
    meta: { requiresAuth: true }
  },
  
  // Admin routes (require admin role)
  { 
    path: '/admin', 
    name: 'admin', 
    component: () => import('../views/admin/AdminDashboard.vue'),
    meta: { requiresAuth: true, requiresAdmin: true }
  },
  { 
    path: '/admin/news', 
    name: 'admin-news', 
    component: () => import('../views/admin/ManageNews.vue'),
    meta: { requiresAuth: true, requiresAdmin: true }
  },
  { 
    path: '/admin/announcements', 
    name: 'admin-announcements', 
    component: () => import('../views/admin/ManageAnnouncements.vue'),
    meta: { requiresAuth: true, requiresAdmin: true }
  },
  { 
    path: '/admin/events', 
    name: 'admin-events', 
    component: () => import('../views/admin/ManageEvents.vue'),
    meta: { requiresAuth: true, requiresAdmin: true }
  },
  { 
    path: '/admin/members', 
    name: 'admin-members', 
    component: () => import('../views/admin/AdminMembers.vue'),
    meta: { requiresAuth: true, requiresAdmin: true }
  },
  
  // Other
  { path: '/site-guide', name: 'site-guide', component: () => import('../views/SiteGuide.vue') }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

// Navigation guards
router.beforeEach(async (to, from, next) => {
  const authStore = useAuthStore();
  
  // Try to fetch profile if not already authenticated
  if (!authStore.isAuthenticated && !authStore.isLoading) {
    await authStore.fetchProfile();
  }
  
  // Check if route requires authentication
  if (to.meta.requiresAuth && !authStore.isAuthenticated) {
    next({ name: 'login', query: { redirect: to.fullPath } });
    return;
  }
  
  // Check if route requires admin
  if (to.meta.requiresAdmin && !authStore.isAdmin) {
    next({ name: 'home' });
    return;
  }
  
  // Redirect authenticated users away from guest pages
  if (to.meta.guest && authStore.isAuthenticated) {
    next({ name: 'dashboard' });
    return;
  }
  
  next();
});

export default router;


