<template>
  <div class="register-container" style="min-height: 80vh; padding: 40px 20px;">
    <div class="container-xl">
      <div class="row justify-content-center">
        <div class="col-md-6">
          <div class="register-card" style="background: linear-gradient(135deg, #ffffff 0%, #f8fbff 100%); border-radius: 30px; padding: 40px; box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1);">
            <div class="register-header text-center mb-4">
              <i class="fa fa-user-plus col_blue" style="font-size: 60px; margin-bottom: 20px;"></i>
              <h2>ایجاد حساب کاربری</h2>
              <p class="text-muted">عضویت در انجمن علمی ریه کودکان</p>
            </div>
            
            <div v-if="registerMessage" :class="'alert alert-' + (registerSuccess ? 'success' : 'danger') + ' alert-dismissible fade show'" role="alert" style="border-radius: 15px;">
              <i :class="(registerSuccess ? 'fa fa-check-circle' : 'fa fa-exclamation-circle') + ' me-2'"></i>{{ registerMessage }}
              <button type="button" class="btn-close" @click="registerMessage = ''"></button>
            </div>
            
            <form @submit.prevent="handleRegister">
              <div class="row">
                <div class="col-md-6 mb-3">
                  <label class="form-label"><i class="fa fa-user me-2 col_blue"></i>نام</label>
                  <input type="text" class="form-control" v-model="registerForm.first_name" placeholder="نام" required style="border-radius: 15px; padding: 12px;">
                </div>
                <div class="col-md-6 mb-3">
                  <label class="form-label"><i class="fa fa-user me-2 col_blue"></i>نام خانوادگی</label>
                  <input type="text" class="form-control" v-model="registerForm.last_name" placeholder="نام خانوادگی" required style="border-radius: 15px; padding: 12px;">
                </div>
              </div>
              
              <div class="mb-3">
                <label class="form-label"><i class="fa fa-at me-2 col_blue"></i>نام کاربری</label>
                <input type="text" class="form-control" v-model="registerForm.username" placeholder="نام کاربری" required style="border-radius: 15px; padding: 12px;">
              </div>
              
              <div class="mb-3">
                <label class="form-label"><i class="fa fa-envelope me-2 col_blue"></i>ایمیل (اختیاری)</label>
                <input type="email" class="form-control" v-model="registerForm.email" placeholder="ایمیل" style="border-radius: 15px; padding: 12px;">
              </div>
              
              <div class="mb-3">
                <label class="form-label"><i class="fa fa-phone me-2 col_blue"></i>شماره تلفن (اختیاری)</label>
                <input type="text" class="form-control" v-model="registerForm.phone" placeholder="شماره تلفن" style="border-radius: 15px; padding: 12px;">
              </div>
              
              <div class="row">
                <div class="col-md-6 mb-3">
                  <label class="form-label"><i class="fa fa-lock me-2 col_blue"></i>رمز عبور</label>
                  <input type="password" class="form-control" v-model="registerForm.password" placeholder="رمز عبور" required style="border-radius: 15px; padding: 12px;">
                </div>
                <div class="col-md-6 mb-3">
                  <label class="form-label"><i class="fa fa-lock me-2 col_blue"></i>تکرار رمز عبور</label>
                  <input type="password" class="form-control" v-model="registerForm.password_confirm" placeholder="تکرار رمز عبور" required style="border-radius: 15px; padding: 12px;">
                </div>
              </div>
              
              <div class="d-grid gap-2">
                <button type="submit" class="btn btn-primary" :disabled="registerLoading" style="border-radius: 15px; padding: 12px; font-weight: 600;">
                  <i v-if="registerLoading" class="fa fa-spinner fa-spin me-2"></i>
                  <i v-else class="fa fa-user-plus me-2"></i>
                  {{ registerLoading ? 'در حال ثبت نام...' : 'ثبت نام' }}
                </button>
              </div>
            </form>
            
            <div class="text-center mt-3">
              <small class="text-muted">حساب کاربری دارید؟ <router-link to="/" class="text-primary text-decoration-none">ورود</router-link></small>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { getApiUrl } from '@/utils/api';

const router = useRouter();

const registerForm = ref({
  username: '',
  email: '',
  phone: '',
  first_name: '',
  last_name: '',
  password: '',
  password_confirm: ''
});

const registerLoading = ref(false);
const registerMessage = ref('');
const registerSuccess = ref(false);

const handleRegister = async () => {
  if (registerForm.value.password !== registerForm.value.password_confirm) {
    registerMessage.value = 'رمزهای عبور مطابقت ندارند';
    registerSuccess.value = false;
    return;
  }
  
  registerLoading.value = true;
  registerMessage.value = '';
  
  try {
    const response = await fetch(getApiUrl('/api/accounts/register/'), {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      credentials: 'include',
      body: JSON.stringify(registerForm.value)
    });
    
    const data = await response.json();
    
    if (data.success) {
      registerSuccess.value = true;
      registerMessage.value = data.message || 'ثبت نام موفقیت‌آمیز بود';
      setTimeout(() => {
        router.push('/dashboard');
      }, 1000);
    } else {
      registerSuccess.value = false;
      if (data.errors) {
        if (typeof data.errors === 'string') {
          registerMessage.value = data.errors;
        } else {
          const firstError = Object.values(data.errors)[0];
          registerMessage.value = Array.isArray(firstError) ? firstError[0] : firstError;
        }
      } else {
        registerMessage.value = 'خطا در ثبت نام';
      }
    }
  } catch (error) {
    registerSuccess.value = false;
    registerMessage.value = 'خطا در ارتباط با سرور';
  } finally {
    registerLoading.value = false;
  }
};
</script>

<style scoped>
.register-container {
  background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
}
</style>

