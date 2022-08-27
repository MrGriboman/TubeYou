<template>
  <HeaderView/>
  <AsideView/>
  <main class="md:ml-24 xl:ml-64 pt-20 px-5 pb-5 grid max-w-screen-2xl m-auto">
    <form class="max-w-screen-2xl">
      <div class="flex">
        <div class="w-1/2">
          <div class="pt-3 pb-3 pl-2 font-bold uppercase bg-red-100 rounded">Изменить аватарку и шапку канала</div>
          <div class="flex pt-5">
            <div class="flex justify-center pr-5">
              <div class="mb-3 w-96 pl-5">
                <label class="form-label inline-block mb-2 text-gray-700 text-xs font-bold uppercase">Выберите аватарку</label>
                <input class="form-control block w-full px-2 py-1 text-sm font-normal text-gray-700 bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" id="" type="file" ref="avatar1" @change="selectAvatar">
              </div>
            </div>
            <button type="button" class="inline-block px-6 border-2 border-pink-400 text-pink-400 font-medium text-xs leading-tight uppercase rounded-xl hover:bg-black hover:bg-opacity-5 focus:outline-none focus:ring-0" @click="changeChannelAvatar">Применить</button>
          </div>
          <div class="pt-5 flex">
            <div class="flex flex-col">
              <div class="mb-3 w-96">
                <label class="form-label inline-block mb-2 text-gray-700 text-xs font-bold uppercase">Выберите шапку</label>
                <input class="form-control block w-full px-2 py-1 text-sm font-normal text-gray-700 bg-clip-padding border border-solid border-gray-300 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" id="" type="file" ref="header1" @change="selectHeader">
              </div>
              <button type="button" class="inline-block pt-5 pb-5 px-10 border-2 border-pink-400 text-pink-400 font-medium text-xs leading-tight uppercase rounded-xl hover:bg-black hover:bg-opacity-5 focus:outline-none focus:ring-0" @click="changeChannelHeader">Применить</button>
            </div>
          </div>
        </div>
      </div>
    </form>
    <form class="max-w-screen-2xl pt-7">
      <div class="font-bold uppercase pt-3 pb-3 pl-2 bg-red-100 rounded w-1/2">Добавить видео</div>
      <div class="flex pb-5 pt-5">
        <div class="w-1/2">
          <div class="flex flex-wrap -mx-3 mb-3">
            <div class="w-full w-full px-3 pr-10">
              <label class="block uppercase text-gray-700 text-xs font-bold mb-2">
                Название
              </label>
              <input class="appearance-none block w-full text-gray-700 border border-red-500 rounded py-3 px-4 mb-3 leading-tight focus:outline-none focus:bg-white" id="" type="text" v-model="videoName">
            </div>
          </div>
          <div class="flex justify-start">
            <div class="mb-3 w-96">
              <label for="formFileLg" class="form-label inline-block mb-2 text-gray-700 block uppercase text-xs font-bold">Превью</label>
              <input class="form-control block w-fullpx-2 py-1.5 text-xl font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-red-500 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" id="" type="file" ref="preview" @change="selectPreview">
            </div>
          </div>
          <div class="flex justify-start">
            <div class="mb-3 w-96">
              <label for="formFileLg" class="form-label inline-block mb-2 text-gray-700 block uppercase text-xs font-bold">Видео</label>
              <input class="form-control block w-fullpx-2 py-1.5 text-xl font-normal text-gray-700 bg-white bg-clip-padding border border-solid border-red-500 rounded transition ease-in-out m-0 focus:text-gray-700 focus:bg-white focus:border-blue-600 focus:outline-none" id="" type="file" ref="file" @change="selectFile">
            </div>
          </div>
        </div>
        <div class="w-1/2 pb-5">
          <label class="block uppercase text-gray-700 text-xs font-bold pb-2">Описание</label>
          <textarea class="w-full h-full p-3 font-medium border border-solid border-gray-300 focus:border-gray-600 focus:outline-none resize-none" v-model="description"></textarea>
        </div>
      </div>
      <button type="button" class="w-full inline-block px-6 py-2.5 bg-pink-500 text-white font-medium text-xs uppercase rounded shadow-lg hover:shadow-lg active:bg-pink-700 active:shadow-lg focus:outline-none transition duration-150 ease-in-out" v-if="document && preview && videoName" @click="upload">Добавить</button>
    </form>
  </main>
  <main class="hidden md:ml-24 xl:ml-64 pt-20 px-5 pb-5 grid max-w-screen-2xl m-auto">
    <div class="font-bold uppercase flex justify-center h-1/2">
      Пожалуйста, авторизируйтесь!
    </div>
  </main>
</template>

<script>
import HeaderView from './HeaderView.vue'
import AsideView from './AsideView.vue'
import axios from 'axios'
import VueAxios from 'vue-axios'

export default {
  components: {
    HeaderView,
    AsideView,
  },

  data() {
    return {
      message: '',
      progress: 0,
      header: null,
      avatar: null,
      document: null,
      preview: null,
      videoName: '',
      description: '',
    }
  },

  methods: {
    selectHeader() {
      this.header = this.$refs.header1.files.item(0)
    },

    selectAvatar() {
      this.avatar = this.$refs.avatar1.files.item(0)
    },

    selectFile() {
      this.document = this.$refs.file.files.item(0)
      console.log(this.document)
    },

    selectPreview() {
      this.preview = this.$refs.preview.files.item(0)
      console.log(this.preview)
    },

    async upload() {
      const headers = {
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Token ' + localStorage.getItem('authToken')
      }
      let formData = new FormData()
      formData.append('name', this.videoName)
      formData.append('video', this.document)
      formData.append('preview', this.preview)
      formData.append('description', this.description)      

      this.videoName = ""
      this.$refs.file.value = null
      this.$refs.preview.value = null;
      this.description = ""

      await axios.post('http://localhost:8000/api/v1/addvideo/', formData, {headers})
        .catch(error => {
          console.log(error.response)
        })
    },

    async changeChannelAvatar() {
      if (this.avatar) {
        const headers = {
          'Content-Type': 'multipart/form-data',
          'Authorization': 'Token ' + localStorage.getItem('authToken')
        }
        await axios.post('http://localhost:8000/api/v1/userinfo/', {avatar: this.avatar}, {headers})
          .then(response => {
            console.log(response)
          })
          .catch(error => {
            console.log(error.response)
          })
        }
    },

    async changeChannelHeader() {
      if (this.header) {
        const headers = {
          'Content-Type': 'multipart/form-data',
          'Authorization': 'Token ' + localStorage.getItem('authToken')
        }
        await axios.post('http://localhost:8000/api/v1/userinfo/', {header: this.header}, {headers})
          .then(response => {
            console.log(response)
            console.log(this.header)
          })
          .catch(error => {
            console.log(error.response)
          })
      }
    },
  },

};
</script>

<style>

</style>
