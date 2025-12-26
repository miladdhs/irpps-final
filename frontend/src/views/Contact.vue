<template>
  <div class="contact-view position-relative">
    <span class="contact-bubble bubble-1 blurred-bubble"></span>
    <span class="contact-bubble bubble-2 blurred-bubble"></span>

    <section id="contact-hero" class="contact-hero-section page-hero glass-section pt-5 pb-5 mb-4">
      <div class="container-xl">
        <div class="row align-items-center min-vh-80">
          <div class="col-md-6">
            <div class="contact-hero-content animate__animated animate__fadeInRight">
              <span class="soft-badge mb-3"><i class="fa fa-comments"></i> {{ $t('contact.badge') }}</span>
              <h1 class="display-4 fw-bold mb-4">{{ $t('contact.title') }}</h1>
              <p class="lead mb-4">{{ $t('contact.subtitle') }}</p>
              <p class="mb-4 text-muted">{{ $t('contact.description') }}</p>
              <div class="contact-hero-buttons d-flex flex-wrap gap-2">
                <a class="soft-button primary animate__animated animate__pulse" href="#contact-info">
                  <i class="fa fa-phone"></i>
                  {{ $t('contact.contactInfo') }}
                </a>
                <a class="soft-button outline" href="#contact-form">
                  <i class="fa fa-envelope"></i>
                  {{ $t('contact.contactForm') }}
                </a>
              </div>
            </div>
          </div>
          <div class="col-md-6">
            <div class="contact-hero-image animate__animated animate__fadeInLeft">
              <div class="contact-hero-image-wrapper image-frame image-frame--wide">
                <img src="/img/hero-contact.svg" class="img-fluid" alt="تماس با ما">
                <div class="floating-elements">
                  <div class="floating-icon floating-icon-1">
                    <i class="fa fa-phone"></i>
                  </div>
                  <div class="floating-icon floating-icon-2">
                    <i class="fa fa-envelope"></i>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="contact-info" class="p_3 glass-section mb-4">
      <div class="container-xl">
        <div class="row">
          <div class="col-md-12 text-center mb-5 section-heading">
            <h2 class="display-5 fw-bold mb-4 animate__animated animate__fadeInUp">{{ $t('contact.contactInfoTitle') }}</h2>
            <p class="lead animate__animated animate__fadeInUp animate__delay-1s">{{ $t('contact.contactInfoSubtitle') }}</p>
          </div>
        </div>
        <div class="row g-4">
          <div class="col-md-4" v-for="(info, index) in contactCards" :key="info.title">
            <div class="contact-info-card glass-card text-center p-4 animate__animated animate__fadeInUp" :class="'animate__delay-' + (index + 2) + 's'">
              <div class="contact-icon mb-4">
                <i :class="'fa fa-3x col_blue ' + info.icon"></i>
              </div>
              <h5 class="fw-bold mb-3">{{ info.title }}</h5>
              <p class="text-muted mb-3">{{ info.subtitle }}</p>
              <div class="contact-details">
                <p v-for="(line, lineIndex) in info.lines" :key="lineIndex" class="mb-2">{{ line }}</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="contact-form" class="p_3 glass-section mb-4">
      <div class="container-xl">
        <div class="row">
          <div class="col-md-12 text-center mb-5 section-heading">
            <h2 class="display-5 fw-bold mb-4 animate__animated animate__fadeInUp">{{ $t('contact.contactFormTitle') }}</h2>
            <p class="lead animate__animated animate__fadeInUp animate__delay-1s">{{ $t('contact.contactFormSubtitle') }}</p>
          </div>
        </div>
        <div class="row justify-content-center">
          <div class="col-md-8">
            <div class="contact-form-wrapper glass-card p-5 animate__animated animate__fadeInUp animate__delay-2s">
              <form class="contact-form" @submit.prevent="handleSubmit">
                <div class="row g-3">
                  <div class="col-md-6">
                    <div class="form-group">
                      <label for="firstName" class="form-label fw-bold">{{ $t('contact.firstName') }}</label>
                      <input type="text" class="form-control modern-input" id="firstName" v-model="form.firstName" :placeholder="$t('contact.firstNamePlaceholder')" required>
                    </div>
                  </div>
                  <div class="col-md-6">
                    <div class="form-group">
                      <label for="lastName" class="form-label fw-bold">{{ $t('contact.lastName') }}</label>
                      <input type="text" class="form-control modern-input" id="lastName" v-model="form.lastName" :placeholder="$t('contact.lastNamePlaceholder')" required>
                    </div>
                  </div>
                  <div class="col-md-6">
                    <div class="form-group">
                      <label for="email" class="form-label fw-bold">{{ $t('contact.emailAddress') }}</label>
                      <input type="email" class="form-control modern-input" id="email" v-model="form.email" :placeholder="$t('contact.emailPlaceholder')" required>
                    </div>
                  </div>
                  <div class="col-md-6">
                    <div class="form-group">
                      <label for="phone" class="form-label fw-bold">{{ $t('contact.phoneNumber') }}</label>
                      <input type="tel" class="form-control modern-input" id="phone" v-model="form.phone" :placeholder="$t('contact.phonePlaceholder')" required>
                    </div>
                  </div>
                  <div class="col-md-12">
                    <div class="form-group">
                      <label for="subject" class="form-label fw-bold">{{ $t('contact.subject') }}</label>
                      <select class="form-select modern-input" id="subject" v-model="form.subject" required>
                        <option value="">{{ $t('contact.subjectPlaceholder') }}</option>
                        <option value="consultation">{{ $t('contact.subjectConsultation') }}</option>
                        <option value="membership">{{ $t('contact.subjectMembership') }}</option>
                        <option value="events">{{ $t('contact.subjectEvents') }}</option>
                        <option value="education">{{ $t('contact.subjectEducation') }}</option>
                        <option value="research">{{ $t('contact.subjectResearch') }}</option>
                        <option value="other">{{ $t('contact.subjectOther') }}</option>
                      </select>
                    </div>
                  </div>
                  <div class="col-md-12">
                    <div class="form-group">
                      <label for="message" class="form-label fw-bold">{{ $t('contact.message') }}</label>
                      <textarea class="form-control modern-input" id="message" v-model="form.message" rows="5" :placeholder="$t('contact.messagePlaceholder')" required></textarea>
                    </div>
                  </div>
                  <div class="col-md-12">
                    <div class="form-group">
                      <div class="form-check">
                        <input class="form-check-input" type="checkbox" id="privacy" v-model="form.privacy" required>
                        <label class="form-check-label" for="privacy">
                          {{ $t('contact.privacyAgreement') }} <a href="#" class="text-primary">{{ $t('contact.termsAndConditions') }}</a>
                        </label>
                      </div>
                    </div>
                  </div>
                  <div class="col-md-12 text-center">
                    <button type="submit" class="soft-button primary btn-lg px-5" :disabled="isSubmitting">
                      <i class="fa fa-paper-plane me-2"></i>{{ isSubmitting ? $t('contact.sending') : $t('contact.send') }}
                    </button>
                  </div>
                </div>
              </form>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="faq" class="p_3">
      <div class="container-xl">
        <div class="row">
          <div class="col-md-12 text-center mb-5">
            <h2 class="display-5 fw-bold mb-4 animate__animated animate__fadeInUp">{{ $t('contact.faqTitle') }}</h2>
            <p class="lead animate__animated animate__fadeInUp animate__delay-1s">{{ $t('contact.faqSubtitle') }}</p>
          </div>
        </div>
        <div class="row justify-content-center">
          <div class="col-md-10">
            <div class="accordion" id="faqAccordion">
              <div class="accordion-item animate__animated animate__fadeInUp animate__delay-2s">
                <h2 class="accordion-header" id="faq1">
                  <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapse1" aria-expanded="true" aria-controls="collapse1">
                    {{ $t('contact.faq1Question') }}
                  </button>
                </h2>
                <div id="collapse1" class="accordion-collapse collapse show" aria-labelledby="faq1" data-bs-parent="#faqAccordion">
                  <div class="accordion-body">
                    {{ $t('contact.faq1Answer') }}
                  </div>
                </div>
              </div>
              
              <div class="accordion-item animate__animated animate__fadeInUp animate__delay-3s">
                <h2 class="accordion-header" id="faq2">
                  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse2" aria-expanded="false" aria-controls="collapse2">
                    {{ $t('contact.faq2Question') }}
                  </button>
                </h2>
                <div id="collapse2" class="accordion-collapse collapse" aria-labelledby="faq2" data-bs-parent="#faqAccordion">
                  <div class="accordion-body">
                    {{ $t('contact.faq2Answer') }}
                  </div>
                </div>
              </div>
              
              <div class="accordion-item animate__animated animate__fadeInUp animate__delay-4s">
                <h2 class="accordion-header" id="faq3">
                  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse3" aria-expanded="false" aria-controls="collapse3">
                    {{ $t('contact.faq3Question') }}
                  </button>
                </h2>
                <div id="collapse3" class="accordion-collapse collapse" aria-labelledby="faq3" data-bs-parent="#faqAccordion">
                  <div class="accordion-body">
                    {{ $t('contact.faq3Answer') }}
                  </div>
                </div>
              </div>
              
              <div class="accordion-item animate__animated animate__fadeInUp animate__delay-5s">
                <h2 class="accordion-header" id="faq4">
                  <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#collapse4" aria-expanded="false" aria-controls="collapse4">
                    {{ $t('contact.faq4Question') }}
                  </button>
                </h2>
                <div id="collapse4" class="accordion-collapse collapse" aria-labelledby="faq4" data-bs-parent="#faqAccordion">
                  <div class="accordion-body">
                    {{ $t('contact.faq4Answer') }}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup lang="ts">
import { onMounted, reactive, ref, computed } from 'vue';
import { useI18n } from 'vue-i18n';

const { t } = useI18n();

const form = reactive({
  firstName: '',
  lastName: '',
  email: '',
  phone: '',
  subject: '',
  message: '',
  privacy: false
});

const isSubmitting = ref(false);

const contactCards = computed(() => [
  {
    icon: 'fa-phone',
    title: t('contact.phoneTitle'),
    subtitle: t('contact.phoneSubtitle'),
    lines: ['021-12345678', '021-87654321', t('contact.phoneHours')]
  },
  {
    icon: 'fa-envelope',
    title: t('contact.emailTitle'),
    subtitle: t('contact.emailSubtitle'),
    lines: ['info@childrenlung.ir', 'support@childrenlung.ir', t('contact.emailResponse')]
  }
]);

function handleSubmit() {
  isSubmitting.value = true;
  setTimeout(() => {
    alert(t('contact.successMessage'));
    Object.assign(form, {
      firstName: '',
      lastName: '',
      email: '',
      phone: '',
      subject: '',
      message: '',
      privacy: false
    });
    isSubmitting.value = false;
  }, 1000);
}

onMounted(() => {
  const observerOptions = {
    threshold: 0.1,
    rootMargin: '0px 0px -50px 0px'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('animate__animated');
      }
    });
  }, observerOptions);

  document.querySelectorAll('.animate__fadeInUp, .animate__fadeInLeft, .animate__fadeInRight').forEach(el => {
    observer.observe(el);
  });

  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      e.preventDefault();
      const target = document.querySelector((this as HTMLElement).getAttribute('href') || '');
      if (target) {
        target.scrollIntoView({
          behavior: 'smooth',
          block: 'start'
        });
      }
    });
  });
});
</script>

