const iconMap: Record<string, string> = {
  add: 'Plus',
  add_task: 'Tick Square',
  admin_panel_settings: 'Setting',
  article: 'Document',
  arrow_back: 'Arrow - Left',
  badge: 'Profile',
  biotech: 'Activity',
  calendar_today: 'Calendar',
  calendar_month: 'Calendar',
  call: 'Call',
  campaign: 'Discovery',
  category: 'Category',
  check_circle: 'Tick Square',
  chevron_left: 'Arrow - Left 2',
  chevron_right: 'Arrow - Right 2',
  child_care: '3 User',
  clinical_notes: 'Document',
  close: 'Close Square',
  contact_phone: 'Calling',
  delete: 'Delete',
  description: 'Document',
  download: 'Download',
  edit: 'Edit',
  email: 'Message',
  emoji_events: 'Ticket Star',
  error: 'Danger',
  event: 'Calendar',
  expand_more: 'Arrow - Down 2',
  flag: 'Discovery',
  folder: 'Folder',
  group: '3 User',
  groups: '3 User',
  healing: 'Heart',
  health_and_safety: 'Shield Done',
  help: 'Info Circle',
  history: 'Time Circle',
  home: 'Home',
  info: 'Info Circle',
  language: 'Category',
  location_on: 'Location',
  logout: 'Logout',
  mail: 'Message',
  medical_information: 'Info Square',
  medical_services: 'Work',
  menu: 'More Circle',
  menu_book: 'Document',
  newspaper: 'Paper',
  newsmode: 'Paper',
  open_in_new: 'Arrow - Right Square',
  package: 'Bag',
  person: 'Profile',
  person_add: 'Add User',
  person_edit: 'Edit Square',
  person_search: 'Search',
  photo_camera: 'Camera',
  photo_library: 'Image',
  picture_as_pdf: 'Document',
  progress_activity: 'Activity',
  public: 'Discovery',
  pulmonology: 'Activity',
  quiz: 'Info Circle',
  restaurant: 'Category',
  rocket_launch: 'Send',
  schedule: 'Time Circle',
  science: 'Activity',
  school: 'Bag',
  search: 'Search',
  share: 'Send',
  slideshow: 'Image',
  support_agent: 'Chat',
  trending_up: 'Graph',
  verified: 'Shield Done',
  visibility: 'Show',
  web: 'Home',
  volunteer_activism: 'Heart',
  workspace_premium: 'Ticket Star',
  zoom_in: 'Search',
  'fa-arrow-left': 'Arrow - Left',
  'fa-arrow-right': 'Arrow - Right',
  'fa-at': 'Message',
  'fa-bars': 'More Circle',
  'fa-book': 'Document',
  'fa-briefcase': 'Work',
  'fa-bullseye': 'Discovery',
  'fa-calendar': 'Calendar',
  'fa-calendar-check': 'Calendar',
  'fa-calendar-check-o': 'Calendar',
  'fa-calendar-times': 'Time Square',
  'fa-certificate': 'Shield Done',
  'fa-check-circle': 'Tick Square',
  'fa-chevron-left': 'Arrow - Left 2',
  'fa-chevron-right': 'Arrow - Right 2',
  'fa-clock': 'Time Circle',
  'fa-envelope': 'Message',
  'fa-exclamation-circle': 'Danger',
  'fa-exclamation-triangle': 'Danger',
  'fa-eye': 'Show',
  'fa-flask': 'Activity',
  'fa-graduation-cap': 'Bag',
  'fa-heart': 'Heart',
  'fa-heartbeat': 'Heart',
  'fa-info-circle': 'Info Circle',
  'fa-instagram': 'Image',
  'fa-language': 'Category',
  'fa-lightbulb-o': 'Discovery',
  'fa-lock': 'Lock',
  'fa-lungs': 'Activity',
  'fa-map-marker': 'Location',
  'fa-map-marker-alt': 'Location',
  'fa-medkit': 'Shield Done',
  'fa-microphone': 'Voice',
  'fa-microscope': 'Activity',
  'fa-newspaper': 'Paper',
  'fa-phone': 'Call',
  'fa-play-circle': 'Play',
  'fa-search': 'Search',
  'fa-sign-in': 'Login',
  'fa-spinner': 'Activity',
  'fa-star': 'Star',
  'fa-stethoscope': 'Activity',
  'fa-telegram': 'Send',
  'fa-times': 'Close Square',
  'fa-times-circle': 'Close Square',
  'fa-trophy': 'Ticket Star',
  'fa-user': 'Profile',
  'fa-user-md': 'Profile',
  'fa-user-plus': 'Add User',
  'fa-users': '3 User',
}

function normalizeClassToken(token: string) {
  return token.trim().replace(/^fa\s+/, '')
}

function resolveIconName(key: string) {
  return iconMap[key] || iconMap[normalizeClassToken(key)] || 'Info Circle'
}

function buildIconSrc(iconName: string, variant = 'Light') {
  return `/iconly/Svg/${variant}/${iconName}.svg`
}

function createImg(iconName: string, variant?: string) {
  const img = document.createElement('img')
  img.src = buildIconSrc(iconName, variant)
  img.alt = ''
  img.setAttribute('aria-hidden', 'true')
  img.className = 'iconly-img'
  return img
}

function replaceMaterialIcons(root: ParentNode) {
  const nodes = root.querySelectorAll<HTMLElement>('.material-symbols-outlined')
  nodes.forEach((node) => {
    if (node.dataset.iconlyApplied === 'true') return
    const iconKey = node.textContent?.trim() || 'info'
    const iconName = resolveIconName(iconKey)
    node.textContent = ''
    node.dataset.iconlyApplied = 'true'
    node.dataset.iconlyName = iconName
    node.classList.add('iconly-host')
    node.appendChild(createImg(iconName))
  })
}

function replaceFontAwesome(root: ParentNode) {
  const nodes = root.querySelectorAll<HTMLElement>('i.fa, span.fa, div.fa')
  nodes.forEach((node) => {
    if (node.dataset.iconlyApplied === 'true') return
    const faClass = Array.from(node.classList).find((className) => className.startsWith('fa-'))
    const iconName = resolveIconName(faClass || 'fa-info-circle')
    node.dataset.iconlyApplied = 'true'
    node.dataset.iconlyName = iconName
    node.classList.add('iconly-host', 'iconly-fa')
    node.textContent = ''
    node.appendChild(createImg(iconName))
  })
}

function applyIconly(root: ParentNode = document) {
  replaceMaterialIcons(root)
  replaceFontAwesome(root)
}

export function initIconly() {
  const run = () => applyIconly(document)

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', run, { once: true })
  } else {
    run()
  }

  const observer = new MutationObserver((mutations) => {
    for (const mutation of mutations) {
      mutation.addedNodes.forEach((addedNode) => {
        if (addedNode instanceof HTMLElement) {
          applyIconly(addedNode)
        }
      })
      if (mutation.type === 'characterData' && mutation.target.parentElement) {
        applyIconly(mutation.target.parentElement)
      }
    }
  })

  observer.observe(document.body, {
    childList: true,
    subtree: true,
    characterData: true,
  })
}
