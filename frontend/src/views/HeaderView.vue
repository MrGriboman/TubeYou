<template>
  <header class="flex justify-between fixed z-30 w-full bg-white">
    <div class="lg:w-1/4 flex">
      <div class="flex items-center xl:w-64 xl:`bg-white` pl-4">
        <button class="mr-3 sm:ml-2 sm:mr-6">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24"
               stroke="currentColor" stroke-width="2">
            <path stroke-linecap="round" stroke-linejoin="round" d="M4 6h16M4 12h8m-8 6h16"/>
          </svg>
        </button>
        <router-link to="/">
          <svg width="50px" height="50px" viewBox="0 0 48 48" xmlns="http://www.w3.org/2000/svg">
            <defs>
              <linearGradient id="linear-gradient" x1="0.5" x2="0.5" y2="1"
                              gradientUnits="objectBoundingBox">
                <stop offset="0" stop-color="#ff0069"/>
                <stop offset="1" stop-color="#b3002b"/>
              </linearGradient>
              <clipPath id="clip-Video">
                <rect width="48" height="48"/>
              </clipPath>
            </defs>
            <g id="Video" clip-path="url(#clip-Video)">
              <rect width="48" height="48" fill="rgba(255,255,255,0)"/>
              <g id="Video-2" data-name="Video" transform="translate(4 12)">
                <g id="Icon" transform="translate(26)" stroke-miterlimit="10"
                   fill="url(#linear-gradient)">
                  <path
                    d="M0,13.6a2,2,0,0,0,.891,1.665l10,6.661A2,2,0,0,0,14,20.265V3.735a2,2,0,0,0-3.109-1.665l-10,6.661A2,2,0,0,0,0,10.4Z"
                    stroke="none"/>
                  <path
                    d="M 11.99444007873535 22.26802062988281 L 11.99442005157471 21.76802062988281 L 11.99450016021729 21.76802062988281 C 12.71852970123291 21.76802062988281 13.5 21.19325065612793 13.5 20.2646598815918 L 13.5 3.735340118408203 C 13.5 2.806750059127808 12.71842956542969 2.231980085372925 11.99431037902832 2.231980085372925 C 11.70028018951416 2.231980085372925 11.4224100112915 2.317759990692139 11.16841983795166 2.486949920654297 L 1.16841995716095 9.14818000793457 C 0.7498800158500671 9.426980018615723 0.5 9.893670082092285 0.5 10.39657020568848 L 0.5 13.60342979431152 C 0.5 14.10632991790771 0.7498800158500671 14.57301998138428 1.16841995716095 14.85181999206543 L 11.16841983795166 21.5130500793457 C 11.41880035400391 21.67983055114746 11.70440006256104 21.76799964904785 11.99435997009277 21.76802062988281 L 11.99444007873535 22.26802062988281 M 11.9943151473999 22.26802062988281 C 11.62259006500244 22.26798629760742 11.2412052154541 22.16230583190918 10.8912296295166 21.92918014526367 L 0.8912299871444702 15.2679500579834 C 0.3344700038433075 14.89708042144775 -8.881784197001252e-16 14.27241039276123 -8.881784197001252e-16 13.60342979431152 L -8.881784197001252e-16 10.39657020568848 C -8.881784197001252e-16 9.72758960723877 0.3344700038433075 9.102919578552246 0.8912299871444702 8.732049942016602 L 10.8912296295166 2.070820093154907 C 11.241286277771 1.837640404701233 11.62250804901123 1.731979131698608 11.9943151473999 1.731979131698608 C 13.03425407409668 1.731979131698608 14 2.558899879455566 14 3.735340118408203 L 14 20.2646598815918 C 14 21.44119834899902 13.03435230255127 22.26811599731445 11.9943151473999 22.26802062988281 Z"
                    stroke="none" fill="rgba(255,255,255,0.3)"/>
                </g>
                <g id="Icon-2" data-name="Icon" fill="rgba(255,125,148,0.6)"
                   stroke="rgba(255,255,255,0.3)"
                   stroke-miterlimit="10" stroke-width="0.5">
                  <rect width="32" height="24" rx="2" stroke="none"/>
                  <rect x="0.25" y="0.25" width="31.5" height="23.5" rx="1.75" fill="none"/>
                </g>
                <path id="Icon-3" data-name="Icon"
                      d="M7,2.5A2.5,2.5,0,1,1,9.5,5,2.5,2.5,0,0,1,7,2.5Zm-7,0A2.5,2.5,0,1,1,2.5,5,2.5,2.5,0,0,1,0,2.5Z"
                      transform="translate(4 4)" fill="#fff"/>
              </g>
            </g>
          </svg>
        </router-link>
      </div>
    </div>
    <div
      class="hidden sm:flex items-center justify-end p-2 pl-8 md:pl-12 md:px-8 flex-1 ld:px-0 lg:w-1/2 max-w-screen-md">
      <div class="flex w-full h-full">
        <input type="text" placeholder="Поиск"
               class="w-full h-9 px-3 shadow rounded-bl-sm rounded-tl-sm border border-gray-300 ml-2 focus:border-red-700 focus:outline-none"
               v-model="searchInput"
               @keyup.enter="search">
        <button
          class=" flex items-center h-9 px-5 mr-2 shadow text-gray-700 bg-gray-100 border border-l-0 border-gray-300 rounded-tr-sm rounded-br-sm hover:bg-gray-300"
          @click="search()">
          <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20"
               xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd"
                  d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
                  clip-rule="evenodd"></path>
          </svg>
        </button>
      </div>
    </div>
    <div class="flex items-center justify-end lg:w-1/4 p-2 sm:px-4">
      <button class="sm:hidden mr-3">
        <svg class="w-6 h-6" fill="currentColor" viewBox="0 0 20 20"
             xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd"
                d="M8 4a4 4 0 100 8 4 4 0 000-8zM2 8a6 6 0 1110.89 3.476l4.817 4.817a1 1 0 01-1.414 1.414l-4.816-4.816A6 6 0 012 8z"
                clip-rule="evenodd"></path>
        </svg>
      </button>
      <router-link to="/login">
        <button
          class="flex items-center whitespace-nowrap px-2 py-1 mr-4 text-sm text-red-700 uppercase border border-red-700 rounded-sm hover:bg-pink-100"
          v-if="!authorized">
          <svg class="mr-2 w-7 h-7" fill="currentColor" viewBox="0 0 20 20"
               xmlns="http://www.w3.org/2000/svg">
            <path fill-rule="evenodd"
                  d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-6-3a2 2 0 11-4 0 2 2 0 014 0zm-2 4a5 5 0 00-4.546 2.916A5.986 5.986 0 0010 16a5.986 5.986 0 004.546-2.084A5 5 0 0010 11z"
                  clip-rule="evenodd"></path>
          </svg>
          Авторизация
        </button>
      </router-link>
      <button
        class="flex items-center whitespace-nowrap px-2 py-1 mr-4 text-sm text-red-700 uppercase border border-red-700 rounded-sm hover:bg-pink-100"
        v-if="authorized"
        @click="logout">
        <svg class="mr-2 w-7 h-7" fill="currentColor" viewBox="0 0 20 20"
             xmlns="http://www.w3.org/2000/svg">
          <path fill-rule="evenodd"
                d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-6-3a2 2 0 11-4 0 2 2 0 014 0zm-2 4a5 5 0 00-4.546 2.916A5.986 5.986 0 0010 16a5.986 5.986 0 004.546-2.084A5 5 0 0010 11z"
                clip-rule="evenodd"></path>
        </svg>
        Выйти
      </button>
    </div>
  </header>
</template>

<script>
import axios from 'axios';
import VueAxios from 'vue-axios'
export default {
  methods: {
    search() {
      if (this.searchInput != null) {
        localStorage.setItem('searchInput', this.searchInput);
        window.location.href = '/';
      }
    },

    logout() {
      const token = 'Token ' + localStorage.getItem('authToken')
      const headers = {
        'Authorization': token
      }
      axios.post('http://localhost:8000/api/v1/auth/token/logout/', {}, {headers})
        .then(response => {          
          localStorage.removeItem('authToken')
           window.location.href = '/'
        })
        .catch(error => {
          console.log(error.response)
          this.authorized = false
          localStorage.removeItem('authToken')
          window.location.href = '/'
        })
    }
  },

  data() {
    return {
      searchInput: '',
      authorized: false,
    };
  },

  async mounted() {
    this.authorized = localStorage.getItem('authToken') ? true : false
  },

};
</script>

<style>
</style>
