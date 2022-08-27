<template>
  <HeaderView/>
  <AsideView/>
  <main class="md:ml-24 xl:ml-64 pt-14">
    <div class="h-20 sm:h-32 xl:h-52 bg-center bg-cover relavite" :style="{backgroundImage: `url(${this.info.header})`}"></div>
    <div class="px-20 pt-4 bg-grey-600 bg-gray-100">
      <div class="flex flex-col sm:flex-row justify-between items-start md:items-center mb-4">
        <div class="flex md:items-center">
          <div class="w-16 h-16 rounded-full mr-4 hidden sm:inline" :style="{backgroundImage: `url(${this.info.avatar})`}"></div>
          <div>
            <div class="flex items-center">
              <textarea id="nicknameid" class="text-2xl text-gray-700 resize-none" :disabled="canEditNick">{{this.info.nickname}}</textarea>
              <button @click="changeChannelNick">
                <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
                  <path strokeLinecap="round" strokeLinejoin="round" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" />
                </svg>
              </button>
            </div>
            <div class="text-sm"></div>
          </div>
        </div>
        <button class="bg-red-700 text-white text-xs uppercase mt-2 xl:mt-0 py-2 px-4 rounded-sm" >Подписаться</button>
      </div>
      <div class="flex pb-5">
        <nav class="mt-2">
          <router-link to="/channel/:id" class="px-6 uppercase text-xs font-medium text-gray-500 hover:text-gray-900 py-2">О канале</router-link>
        </nav>
        <nav class="mt-2">
          <router-link to="/channel/videos/:id" class="px-6 uppercase text-xs font-medium text-gray-500 hover:text-gray-900 py-2">Видео</router-link>
        </nav>
        <div></div>
      </div>
    </div>
    <div class="flex m-5 pt-6">
      <button @click="changeChannelInfo">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" strokeWidth={2}>
          <path strokeLinecap="round" strokeLinejoin="round" d="M15.232 5.232l3.536 3.536m-2.036-5.036a2.5 2.5 0 113.536 3.536L6.5 21.036H3v-3.572L16.732 3.732z" />
        </svg>
      </button>
      <textarea id="description"  class="w-full h-full p-3 font-medium border border-solid border-gray-300 focus:border-gray-600 focus:outline-none resize-none" :disabled="canEdit">{{this.info.description}}</textarea>
    </div>
  </main>
  <main class="hidden md:ml-24 xl:ml-64 pt-20 px-5 pb-5 grid max-w-screen-2xl m-auto">
    <div class="font-bold uppercase flex justify-center h-1/2">
      Пожалуйста, авторизируйтесь!
    </div>
  </main>
</template>

<script>
import HeaderView from './HeaderView.vue';
import AsideView from './AsideView.vue';
import axios from 'axios'
import VueAxios from 'vue-axios'
export default {
  components: {
    HeaderView,
    AsideView,
  },
  data() {
    return {
      canEdit: {
        type: Boolean,
        default: false,
      },
      canEditNick: {
        type: Boolean,
        default: false,
      },
      info: [],
      channelDescription: '',
    };
  },
  methods: {
   async changeChannelInfo() {
     if(!this.canEdit) {
       this.channelDescription = document.getElementById('description').value
       const headers = {
         'Authorization': 'Token ' + localStorage.getItem('authToken')
       }
       await axios.post('http://localhost:8000/api/v1/userinfo/', {description: this.channelDescription}, {headers})
         .then(response => {
           console.log(response)
         })
         .catch(error => {
           console.log(error.response)
         })
     }
     this.canEdit = !this.canEdit;
   },
   async changeChannelNick() {
     if(!this.canEditNick) {
       this.channelNick = document.getElementById('nicknameid').value
       const headers = {
         'Authorization': 'Token ' + localStorage.getItem('authToken')
       }
       await axios.post('http://localhost:8000/api/v1/userinfo/', {nickname: this.channelNick}, {headers})
         .then(response => {
           console.log(response)
         })
         .catch(error => {
           console.log(error.response)
         })
     }
     this.canEditNick = !this.canEditNick;
   },
 },
  async created() {    
    const token = 'Token ' + localStorage.getItem('authToken')
    const headers = {
      'Authorization': token
    }
    await axios.get('http://localhost:8000/api/v1/userinfo/?getme=1', {headers})
      .then(response => {
        this.info = response.data[0]
        if (!this.info.header)
          this.info.header = require('../assets/image.jpg')
        if (!this.info.avatar)
          this.info.avatar = require('../assets/bg.jpg')
      }) 
      .catch(error => {
        console.log(error.response)
      })
  }
};
</script>

<style scoped>
.router-link-active{
  @apply border-b-2 border-gray-300 text-gray-900;
}
#description {
  height: 250px;
}
#nicknameid {
    height: 40px;
    overflow: hidden;
}
</style>