<template>
    <v-app>
      <v-main>
        <v-container>
        <v-card>
          <v-card-title>
            Street Fighter 2 勝敗記録アプリ
          </v-card-title>
        <Table :memos="memos"  :charas="charas" :results="results" v-on:editItem="editItem" v-on:deleteItem="deleteItem"/>
        <Create :newitem="newitem" :charas="charas" :results="results" v-on:createItem="createItem" />
        </v-card>
        </v-container>
      </v-main>
    </v-app>
</template>


<script>
import Create from '~/components/Create.vue';
import Table from '~/components/Table.vue';

export default {
    data () {
      return {newitem:{date:'', time:'',result:'', my_chara:'', op_chara:''}
      }},  
    async asyncData({$axios}){
        const memos = await $axios.$get('/memo/')
        const charas = await $axios.$get('/chara/')        
        const results = await $axios.$get('/result/')

        return {memos : memos, charas:charas, results:results}
    },
    methods:{
      async editItem ({item}) {
        this.$axios.$patch("/memo/",item)
        .then((res) => {
            this.memos = res})
      },
      async deleteItem({item}){
        this.$axios.$put("/memo/", item)
        .then((res) => {
            this.memos = res})
      },
      async createItem({newitem}){
        this.$axios.$post("/memo/", newitem)
        .then((res) => {
            this.memos = res
            this.newitem = {date:'', time:'',result:'', my_chara:'', op_chara:''}})
      }
    },
    components:{
      Create:Create,
      Table:Table
    }
}
</script>