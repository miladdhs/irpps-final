import { createI18n } from 'vue-i18n'
import fa from './locales/fa.json'
import en from './locales/en.json'

const messages = {
  fa,
  en
}

// Get initial locale safely (check if window exists for SSR)
const getInitialLocale = () => {
  if (typeof window !== 'undefined') {
    return localStorage.getItem('locale') || 'fa'
  }
  return 'fa'
}

const i18n = createI18n({
  legacy: false,
  locale: getInitialLocale(),
  fallbackLocale: 'fa',
  messages
})

export default i18n

