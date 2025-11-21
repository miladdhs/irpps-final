import { createApp } from 'vue';
import App from './App.vue';
import router from './router';
import i18n from './i18n';

// Import CSS files
import '../css/bootstrap.min.css';
import '../css/font-awesome.min.css';
import '../css/global.css';
import '../css/index.css';
import './assets/ltr-support.css';
// Import vue3-persian-datetime-picker styles
import 'vue3-persian-datetime-picker/src/picker/assets/scss/style.scss';

const app = createApp(App);
app.use(router);
app.use(i18n);
app.mount('#app');


