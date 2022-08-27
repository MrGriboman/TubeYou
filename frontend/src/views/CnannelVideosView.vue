<template>
  <HeaderView/>
  <AsideView/>
  <main class="md:ml-24 xl:ml-64 pt-14 pb-5">
    <div class="h-20 sm:h-32 xl:h-52 bg-center bg-cover" :style="{backgroundImage: `url(${this.info.header})`}"></div>
    <div class="px-20 pt-4 bg-grey-600 bg-gray-100">
      <div class="flex flex-col sm:flex-row justify-between items-start md:items-center mb-4">
        <div class="flex md:items-center">
          <div class="w-16 h-16 rounded-full mr-4 hidden sm:inline" :style="{backgroundImage: `url(${this.info.avatar})`}"></div>
          <div>
            <div class="flex items-center">
              <span class="text-2xl text-gray-700">{{this.info.nickname}}</span>
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
    <div class="grid gap-4 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 2xl:grid-cols-5 max-w-screen-2xl m-auto pt-6 px-5 ">
      <div v-for="video in videos" :key="video.id">
        <div class="relative mb-3 group">
          <router-link :to="{name: 'video', params: {id: video.id}}">
            <img :src="`${video.preview}`" :alt="X" class="object-cover aspect-video">
          </router-link>
        </div>
        <div class="flex item-start mt-3 group">
          <img :src="`${ video.avatar}`" class="mr-3 rounded-full w-9 h-9" alt="">
          <div class="text-sm">
            <router-link :to="{name: 'video', params: {id: video.id}}">
              <span class="font-semibold text-gray-800">{{ video.name }}</span>
            </router-link>
            <div class="mt-1 flex items-center">
              <span>{{ video.author_name }}</span>
            </div>
            <div>
              <span>{{ video.views }}</span>
              &middot;
              <span>{{ format(video.upload_time) }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </main>
</template>

<script>
import HeaderView from './HeaderView.vue'
import AsideView from './AsideView.vue'
import ChannelView from './ChannelView.vue'
import dayjs from "@/utils/dayjs"
import axios from 'axios'
import VueAxios from 'vue-axios'

export default {
  methods: {
    format(data) {
      return dayjs(data, 'YYYY-MM-DD hh:mm:ss').fromNow(true)
    },
  },
  data() {
    return {
      videos: [],
      info: [],
    };
  },
  async created() {

    const token = 'Token ' + localStorage.getItem('authToken')
    const headers = {
      'Authorization': token
    }

    await axios.get('http://localhost:8000/api/v1/userinfo/?getuservideo=1', {headers})
      .then(response => {
        this.videos = response.data        
        for (var i = 0; i < this.videos.length; i++) {
          this.videos[i].preview = 'http://localhost:8000' + this.videos[i].preview            
          if (!this.videos[i].avatar)
            this.videos[i].avatar = require('../assets/bg.jpg')
        }         
      }).catch(error => {
        console.log(error.response)
      })

    await axios.get('http://localhost:8000/api/v1/userinfo/?getme=1', {headers})
      .then(response => {       
        console.log(response.data[0])
        this.info = response.data[0]
        if (!this.info.header)
          this.info.header = require('../assets/image.jpg')
        if (!this.info.avatar)
          this.info.avatar = require('../assets/bg.jpg')
      }) 
      .catch(error => {
        console.log(error.response)
      })
  },
  components: {
    HeaderView,
    AsideView,
  },
};
</script>

<style scoped>
.router-link-active{
  @apply border-b-2 border-gray-300 text-gray-900;
}
</style>
