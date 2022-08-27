<template>
  <div class="banner w-full min-h-screen flex flex-col sm:justify-center items-center pt-6 sm:pt-0" >
    <div class="w-full sm:max-w-md p-5 mx-auto">
      <h2 class="mb-12 text-center text-5xl font-extrabold text-gray-200">Регистрация</h2>
      <form @submit.prevent="register">
        <div class="mb-4">
          <label class="block mb-1 text-gray-200" for="nickname">Никнейм</label>
          <input v-model="formData.username" id="nickname" type="text" name="nickname" class="bg-yellow-50 py-2 px-3 border border-gray-300 focus:border-red-300 focus:outline-none focus:ring focus:ring-yellow-300 focus:ring-opacity-50 rounded-md shadow-sm disabled:bg-gray-100 mt-1 block w-full" />
        </div>
        <div class="mb-4">
          <label class="block mb-1 text-gray-200" for="email">Почта</label>
          <input v-model="formData.email" id="email" type="text" name="email" class="email bg-yellow-50 py-2 px-3 border border-gray-300 focus:border-red-300 focus:outline-none focus:ring focus:ring-yellow-300 focus:ring-opacity-50 rounded-md shadow-sm disabled:bg-gray-100 mt-1 block w-full" />
        </div>
        <div class="mb-4">
          <label class="block mb-1 text-gray-200" for="password">Пароль</label>
          <input v-model="formData.password" id="password" type="password" name="password" class="bg-yellow-50 py-2 px-3 border border-gray-300 focus:border-red-300 focus:outline-none focus:ring focus:ring-yellow-300 focus:ring-opacity-50 rounded-md shadow-sm disabled:bg-gray-100 mt-1 block w-full" />
        </div>
        <div class="mb-4">
          <label class="block mb-1 text-gray-200" for="password">Повторите пароль</label>
          <input v-model="passwordCheck" id="passwordCheck" type="password" name="passwordCheck" class="bg-yellow-50 py-2 px-3 border border-gray-300 focus:border-red-300 focus:outline-none focus:ring focus:ring-yellow-300 focus:ring-opacity-50 rounded-md shadow-sm disabled:bg-gray-100 mt-1 block w-full" />
        </div>
        <div v-show="passwordMismatch" class="text-center text-white">
          <div>Поля «пароль» и «повторите пароль» не совпадают!</div>
        </div>
        <div v-show="blankInputs" class="text-center text-white">
          <div>Поля не могут быть пустыми!</div>
        </div>
        <div v-show="registrationFailed" class="text-center text-gray-200">
          <div class="whitespace-pre-line">Не удалось зарегистрироваться, проверьте следующее:<br>1. E-mail должен быть действителен<br>2. Пароль не должен быть похож на никнейм или E-mail<br>3. Пароль должен состоять как минимум из 8 символов, не состоять только из цифр и не быть слишком простым (напр. qwerty123)
          </div>
        </div>
        <div class="mt-6">
          <button class="w-full inline-flex items-center justify-center px-4 py-2 bg-yellow-700 border border-transparent rounded-md font-semibold capitalize text-white hover:bg-yellow-800 active:bg-red-700 focus:outline-none focus:border-red-700  disabled:opacity-25 transition"
                  type="submit">Зарегистрироваться</button>
        </div>
        <div class="mt-6 text-center text-white">
          <label class="pr-2">Уже есть аккаунт?</label>
          <router-link to="/login" class="underline">Войдите</router-link>
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
        email: '',
        password: '',
      },
      passwordCheck: '',
      passwordMismatch: false,
      blankInputs: false,
      registrationFailed: false,
    }
  },

  methods: {
    register() {
      if (this.formData.username === ''||
        this.formData.email === ''||
        this.formData.password === ''||
        this.passwordCheck === '') {
        this.blankInputs = true;
        this.$forceUpdate()
        return
      }
      if (this.formData.password !== this.passwordCheck){
        this.passwordMismatch = true
        this.$forceUpdate()
        return
      }
      this.passwordMismatch = false
      this.blankInputs = false
      axios.post('http://localhost:8000/api/v1/auth/users/', this.formData)
        .then(response => {
          console.log(response.data)
          this.registrationFailed = false
          window.location.href = '/login'
        })
        .catch(error => {
          console.log(error.request.responseText)
          this.registrationFailed = true
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
