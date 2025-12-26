<template>
  <div class="about-view position-relative">
    <span class="about-bubble bubble-1 blurred-bubble"></span>
    <span class="about-bubble bubble-2 blurred-bubble"></span>

    <section id="about-hero" class="about-hero-section page-hero glass-section pt-5 pb-5 mb-4">
      <div class="container-xl">
        <div class="row align-items-center min-vh-80">
          <div class="col-md-6">
            <div class="about-hero-content animate__animated animate__fadeInRight">
              <span class="soft-badge secondary mb-3">
                <i class="fa fa-heartbeat"></i>
                {{ $t('about.badge') }}
              </span>
              <h1 class="display-4 fw-bold mb-4">{{ $t('about.title') }}</h1>
              <p class="lead mb-4">{{ $t('about.subtitle') }}</p>
              <p class="mb-4 text-muted">{{ $t('about.description') }}</p>
              <div class="about-hero-buttons d-flex flex-wrap gap-2">
                <a class="soft-button primary animate__animated animate__pulse" href="#establishment">
                  <i class="fa fa-arrow-right"></i>
                  {{ $t('about.establishmentTitle') }}
                </a>
                <a class="soft-button outline" href="#founders">
                  <i class="fa fa-users"></i>
                  {{ $t('about.foundersTitle') }}
                </a>
              </div>
            </div>
          </div>
          <div class="col-md-6">
            <div class="about-hero-image animate__animated animate__fadeInLeft">
                <div class="about-hero-image-wrapper image-frame image-frame--wide">
                 <img src="/img/hero-about.svg" class="img-fluid" alt="تصویری نمادین از انجمن علمی ریه کودکان ایران">
                <div class="floating-elements">
                  <div class="floating-icon floating-icon-1">
                    <i class="fa fa-heartbeat"></i>
                  </div>
                  <div class="floating-icon floating-icon-2">
                    <i class="fa fa-stethoscope"></i>
                  </div>
                  <div class="floating-icon floating-icon-3">
                    <i class="fa fa-user-md"></i>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="about-stats" class="p_3 home-stats-section mb-4">
      <div class="container-xl">
        <div class="row text-center">
          <div class="col-md-3 col-sm-6 mb-4">
            <div class="stat-item glass-card animate__animated animate__fadeInUp">
              <div class="stat-icon mb-3">
                <i class="fa fa-user-md fa-2x"></i>
              </div>
              <h2 class="fw-bold counter" data-target="50">0</h2>
              <p class="mb-0">{{ $t('home.stat1') }}</p>
            </div>
          </div>
          <div class="col-md-3 col-sm-6 mb-4">
            <div class="stat-item glass-card animate__animated animate__fadeInUp animate__delay-1s">
              <div class="stat-icon mb-3">
                <i class="fa fa-heart fa-2x"></i>
              </div>
              <h2 class="fw-bold counter" data-target="1000">0</h2>
              <p class="mb-0">{{ $t('home.stat2') }}</p>
            </div>
          </div>
          <div class="col-md-3 col-sm-6 mb-4">
            <div class="stat-item glass-card animate__animated animate__fadeInUp animate__delay-2s">
              <div class="stat-icon mb-3">
                <i class="fa fa-book fa-2x"></i>
              </div>
              <h2 class="fw-bold counter" data-target="25">0</h2>
              <p class="mb-0">{{ $t('home.stat3') }}</p>
            </div>
          </div>
          <div class="col-md-3 col-sm-6 mb-4">
            <div class="stat-item glass-card animate__animated animate__fadeInUp animate__delay-3s">
              <div class="stat-icon mb-3">
                <i class="fa fa-trophy fa-2x"></i>
              </div>
              <h2 class="fw-bold counter" data-target="15">0</h2>
              <p class="mb-0">{{ $t('home.stat4') }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="mission" class="p_3 glass-section mb-4">
      <div class="container-xl">
        <div class="row">
          <div class="col-md-12 text-center mb-5 section-heading">
            <h2 class="display-5 fw-bold mb-4 animate__animated animate__fadeInUp">{{ $t('about.missionTitle') }}</h2>
            <p class="lead animate__animated animate__fadeInUp animate__delay-1s">{{ $t('about.missionSubtitle') }}</p>
          </div>
        </div>
        <div class="row g-4">
          <div class="col-md-6">
            <div class="mission-card glass-card text-center p-5 animate__animated animate__fadeInLeft">
              <div class="mission-icon mb-4">
                <i class="fa fa-bullseye fa-3x col_blue"></i>
              </div>
              <h3 class="fw-bold mb-3">{{ $t('about.ourMission') }}</h3>
              <p class="text-muted">{{ $t('about.missionDescription') }}</p>
            </div>
          </div>
          <div class="col-md-6">
            <div class="vision-card glass-card text-center p-5 animate__animated animate__fadeInRight">
              <div class="vision-icon mb-4">
                <i class="fa fa-eye fa-3x col_blue"></i>
              </div>
              <h3 class="fw-bold mb-3">{{ $t('about.visionTitle') }}</h3>
              <p class="text-muted">{{ $t('about.visionDescription') }}</p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="about-content" class="p_3 glass-section mb-4">
      <div class="container-xl">
        <div class="row align-items-center g-4">
          <div class="col-md-6">
            <div class="about-content-text animate__animated animate__fadeInLeft">
              <h2 class="display-6 fw-bold mb-4">{{ $t('about.activitiesTitle') }}</h2>
              <p class="lead mb-4">{{ $t('about.activitiesLead') }}</p>
              <p class="mb-4 text-muted">{{ $t('about.activitiesDescription') }}</p>
              <div class="about-features">
                <div class="feature-item d-flex align-items-center mb-3 glass-chip">
                  <i class="fa fa-check-circle col_blue me-3 fa-2x"></i>
                  <span>{{ $t('about.activity1') }}</span>
                </div>
                <div class="feature-item d-flex align-items-center mb-3 glass-chip">
                  <i class="fa fa-check-circle col_blue me-3 fa-2x"></i>
                  <span>{{ $t('about.activity2') }}</span>
                </div>
                <div class="feature-item d-flex align-items-center mb-3 glass-chip">
                  <i class="fa fa-check-circle col_blue me-3 fa-2x"></i>
                  <span>{{ $t('about.activity3') }}</span>
                </div>
                <div class="feature-item d-flex align-items-center mb-3 glass-chip">
                  <i class="fa fa-check-circle col_blue me-3 fa-2x"></i>
                  <span>{{ $t('about.activity4') }}</span>
                </div>
              </div>
            </div>
          </div>
          <div class="col-md-6">
            <div class="about-content-image animate__animated animate__fadeInRight">
              <div class="about-image-wrapper image-frame">
                <img src="/img/about-insight.svg" class="img-fluid" alt="فعالیت‌های انجمن علمی ریه کودکان ایران">
                <div class="image-overlay">
                  <div class="overlay-content">
                    <i class="fa fa-play-circle fa-4x text-white"></i>
                    <p class="text-white mt-3">ویدیو معرفی انجمن</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="skills" class="p_3 glass-section mb-4">
      <div class="container-xl">
        <div class="row">
          <div class="col-md-12 text-center mb-5 section-heading">
            <h2 class="display-5 fw-bold mb-4 animate__animated animate__fadeInUp">{{ $t('about.expertiseTitle') }}</h2>
            <p class="lead animate__animated animate__fadeInUp animate__delay-1s">{{ $t('about.expertiseSubtitle') }}</p>
          </div>
        </div>
        <div class="row g-4 align-items-start">
          <div class="col-md-6">
            <div class="skills-content animate__animated animate__fadeInLeft">
              <h3 class="mb-4">{{ $t('about.expertiseHeading') }}</h3>
              <p class="mb-4 text-muted">{{ $t('about.expertiseDescription') }}</p>
              <div class="skill-item glass-card mb-3 p-4">
                <div class="skill-header d-flex justify-content-between mb-2">
                  <span class="fw-bold">{{ $t('about.skill1') }}</span>
                  <span class="text-primary fw-bold">95%</span>
                </div>
                <div class="progress-modern">
                  <div class="progress-bar-modern" style="width: 95%"></div>
                </div>
              </div>
              <div class="skill-item glass-card mb-3 p-4">
                <div class="skill-header d-flex justify-content-between mb-2">
                  <span class="fw-bold">{{ $t('about.skill2') }}</span>
                  <span class="text-primary fw-bold">92%</span>
                </div>
                <div class="progress-modern">
                  <div class="progress-bar-modern" style="width: 92%"></div>
                </div>
              </div>
              <div class="skill-item glass-card mb-3 p-4">
                <div class="skill-header d-flex justify-content-between mb-2">
                  <span class="fw-bold">{{ $t('about.skill3') }}</span>
                  <span class="text-primary fw-bold">88%</span>
                </div>
                <div class="progress-modern">
                  <div class="progress-bar-modern" style="width: 88%"></div>
                </div>
              </div>
              <div class="skill-item glass-card p-4">
                <div class="skill-header d-flex justify-content-between mb-2">
                  <span class="fw-bold">{{ $t('about.skill4') }}</span>
                  <span class="text-primary fw-bold">90%</span>
                </div>
                <div class="progress-modern">
                  <div class="progress-bar-modern" style="width: 90%"></div>
                </div>
              </div>
            </div>
          </div>
          <div class="col-md-6">
            <div class="skills-image animate__animated animate__fadeInRight">
              <div class="skills-image-wrapper image-frame">
                <img src="/img/about-skills.svg" class="img-fluid" alt="تخصص‌های انجمن علمی ریه کودکان ایران">
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Establishment and Goals Section -->
    <section id="establishment" class="p_3 glass-section mb-4">
      <div class="container-xl">
        <div class="row">
          <div class="col-md-12 text-center mb-5 section-heading">
            <h2 class="display-5 fw-bold mb-4 animate__animated animate__fadeInUp">{{ $t('about.establishmentTitle') }}</h2>
            <p class="lead text-primary fw-bold animate__animated animate__fadeInUp animate__delay-1s">
              <i class="fa fa-calendar-check-o me-2"></i>
              {{ $t('about.establishmentDate') }}
            </p>
          </div>
        </div>
        <div class="row mb-5">
          <div class="col-md-12">
            <div class="goals-section glass-card p-5 animate__animated animate__fadeInUp">
              <h3 class="fw-bold mb-4 text-center">
                <i class="fa fa-bullseye col_blue me-2"></i>
                {{ $t('about.goalsTitle') }}
              </h3>
              <div class="row g-3">
                <div class="col-md-6">
                  <div class="goal-item d-flex align-items-start mb-3">
                    <i class="fa fa-check-circle col_blue me-3 mt-1 fa-lg"></i>
                    <span>{{ $t('about.goal1') }}</span>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="goal-item d-flex align-items-start mb-3">
                    <i class="fa fa-check-circle col_blue me-3 mt-1 fa-lg"></i>
                    <span>{{ $t('about.goal2') }}</span>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="goal-item d-flex align-items-start mb-3">
                    <i class="fa fa-check-circle col_blue me-3 mt-1 fa-lg"></i>
                    <span>{{ $t('about.goal3') }}</span>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="goal-item d-flex align-items-start mb-3">
                    <i class="fa fa-check-circle col_blue me-3 mt-1 fa-lg"></i>
                    <span>{{ $t('about.goal4') }}</span>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="goal-item d-flex align-items-start mb-3">
                    <i class="fa fa-check-circle col_blue me-3 mt-1 fa-lg"></i>
                    <span>{{ $t('about.goal5') }}</span>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="goal-item d-flex align-items-start mb-3">
                    <i class="fa fa-check-circle col_blue me-3 mt-1 fa-lg"></i>
                    <span>{{ $t('about.goal6') }}</span>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="goal-item d-flex align-items-start mb-3">
                    <i class="fa fa-check-circle col_blue me-3 mt-1 fa-lg"></i>
                    <span>{{ $t('about.goal7') }}</span>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="goal-item d-flex align-items-start mb-3">
                    <i class="fa fa-check-circle col_blue me-3 mt-1 fa-lg"></i>
                    <span>{{ $t('about.goal8') }}</span>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="goal-item d-flex align-items-start mb-3">
                    <i class="fa fa-check-circle col_blue me-3 mt-1 fa-lg"></i>
                    <span>{{ $t('about.goal9') }}</span>
                  </div>
                </div>
                <div class="col-md-6">
                  <div class="goal-item d-flex align-items-start mb-3">
                    <i class="fa fa-check-circle col_blue me-3 mt-1 fa-lg"></i>
                    <span>{{ $t('about.goal10') }}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Founders Section -->
    <section id="founders" class="p_3 glass-section mb-4">
      <div class="container-xl">
        <div class="row">
          <div class="col-md-12 text-center mb-5 section-heading">
            <h2 class="display-5 fw-bold mb-4 animate__animated animate__fadeInUp">{{ $t('about.foundersTitle') }}</h2>
            <p class="lead animate__animated animate__fadeInUp animate__delay-1s">{{ $t('about.foundersSubtitle') }}</p>
          </div>
        </div>
        <div class="row g-4">
          <div class="col-md-12">
            <div class="founders-card glass-card p-5 animate__animated animate__fadeInUp">
              <div class="row g-4">
                <div class="col-md-6 col-lg-4">
                  <div class="founder-item text-center p-4 glass-chip">
                    <i class="fa fa-user-md col_blue fa-3x mb-3"></i>
                    <h5 class="fw-bold mb-2">دکتر سهیلا خلیل زاده</h5>
                    <span class="badge bg-primary">{{ $t('about.president') }}</span>
                  </div>
                </div>
                <div class="col-md-6 col-lg-4">
                  <div class="founder-item text-center p-4 glass-chip">
                    <i class="fa fa-user-md col_blue fa-3x mb-3"></i>
                    <h5 class="fw-bold mb-2">دکتر قمر تاج خانبابائی</h5>
                    <span class="badge bg-success">{{ $t('about.vicePresident') }}</span>
                  </div>
                </div>
                <div class="col-md-6 col-lg-4">
                  <div class="founder-item text-center p-4 glass-chip">
                    <i class="fa fa-user-md col_blue fa-3x mb-3"></i>
                    <h5 class="fw-bold mb-2">دکتر محمدرضائی</h5>
                    <span class="badge bg-info">{{ $t('about.secretary') }}</span>
                  </div>
                </div>
                <div class="col-md-6 col-lg-4">
                  <div class="founder-item text-center p-4 glass-chip">
                    <i class="fa fa-user-md col_blue fa-3x mb-3"></i>
                    <h5 class="fw-bold mb-2">دکتر مجید کیوانفر</h5>
                    <span class="badge bg-warning text-dark">{{ $t('about.treasurer') }}</span>
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
import { onMounted } from 'vue';

function animateCounter(element: HTMLElement) {
  const target = parseInt(element.getAttribute('data-target') || '0');
  const duration = 1200;
  const increment = target / (duration / 16);
  let current = 0;
  
  const timer = setInterval(() => {
    current += increment;
    if (current >= target) {
      current = target;
      clearInterval(timer);
    }
    element.textContent = Math.floor(current).toString();
  }, 16);
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
        if (entry.target.classList.contains('counter')) {
          animateCounter(entry.target as HTMLElement);
          observer.unobserve(entry.target);
        }
      }
    });
  }, observerOptions);

  document.querySelectorAll('.animate__fadeInUp, .animate__fadeInLeft, .animate__fadeInRight, .counter').forEach(el => {
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

<style scoped>
@media (min-width: 992px) {
  #founders .col-lg-4 {
    flex: 0 0 auto;
    width: 25%;
  }
}
</style>

