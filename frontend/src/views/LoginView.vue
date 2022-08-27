<template>
  <div class="banner w-full min-h-screen flex flex-col sm:justify-center items-center pt-6 sm:pt-0" >
    <div class="w-full sm:max-w-md p-5 mx-auto">
      <h2 class="mb-12 text-center text-5xl font-extrabold text-gray-300">Войти</h2>
      <form @submit.prevent="login">
        <div class="mb-4">
          <label class="block mb-1 text-gray-200" for="nickname">Никнейм</label>
          <input v-model="formData.username" id="nickname" type="text" name="nickname" class="bg-yellow-50 py-2 px-3 border border-gray-300 focus:border-red-300 focus:outline-none focus:ring focus:ring-yellow-300 focus:ring-opacity-50 rounded-md shadow-sm disabled:bg-gray-100 mt-1 block w-full" />
        </div>
        <div class="mb-4">
          <label class="block mb-1 text-gray-200" for="password">Пароль</label>
          <input v-model="formData.password" id="password" type="password" name="password" class="bg-yellow-50 py-2 px-3 border border-gray-300 focus:border-red-300 focus:outline-none focus:ring focus:ring-yellow-300 focus:ring-opacity-50 rounded-md shadow-sm disabled:bg-gray-100 mt-1 block w-full" />
        </div>
        <div class="mt-6">
          <button class="w-full inline-flex items-center justify-center px-4 py-2 bg-yellow-700 border border-transparent rounded-md font-semibold capitalize text-white hover:bg-yellow-800 active:bg-red-700 focus:outline-none focus:border-red-700  disabled:opacity-25 transition">Войти</button>
        </div>
        <div class="text-center text-white">
          <div v-show="loginError">Неверный логин или пароль</div>
        </div>
        <div class="mt-6 text-center text-white">
          <label class="pr-2">Ещё нет аккаунта?</label>
          <router-link to="/register" class="underline">Зарегистрируйтесь</router-link>
        </div>
      </form>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import VueAxios from 'vue-axios'
export default {
  data() {
    return {
      formData: {
        username: '',
        password: '',
      },
      loginError: false,
    }
  },

  methods: {
    login() {
      axios.post('http://localhost:8000/api/v1/auth/token/login/', this.formData)
        .then(response => {
          console.log(response.data.auth_token)
          this.loginError = false
          localStorage.setItem('authToken', response.data.auth_token)
          window.location.href = '/'
        })
        .catch(error => {
          console.log(error.request)
          this.loginError = true
          this.$forceUpdate()
        })
    },

  },
};
</script>

<style>
.banner {
  background: url(http://4.bp.blogspot.com/-v2qV3ee8ikA/Vfu1-fWSGtI/AAAAAAAABrs/hiv3sAkszYo/s1600/Sugar-bag-final-animation.gif);
  background-repeat: no-repeat;
  background-size: cover
}
</style>
