<template>
    <v-container>
          <v-card outlined>
            <v-container>
            <v-row justify="center">
              <v-col>
                <v-text-field v-model="newitem.date" type="date" label="日付"></v-text-field>
              </v-col>
              <v-col>
                <v-text-field v-model="newitem.time" type="time" label="時間"></v-text-field>
              </v-col>
              <v-col>
                <v-select
                      v-model="newitem.result"
                      :items="results"
                      item-text="result" 
                      item-value="id"
                      label="勝敗"
                      ></v-select>
              </v-col>
              <v-col>
                <v-select
                      v-model="newitem.my_chara"
                      :items="charas"
                      item-text="character" 
                      item-value="id"
                      label="自キャラ"
                    ></v-select>
              </v-col>
              <v-col>
                <v-select
                  v-model="newitem.op_chara"
                  :items="charas"
                  item-text="character" 
                  item-value="id"
                  label="相手キャラ"
                ></v-select>
              </v-col>
              <v-col>
                <v-btn  @click="$emit('createItem',{newitem})" >
                 新しいメモを作成  
                </v-btn>
              </v-col>
          </v-row>
          </v-container>
        </v-card>
    </v-container>
</template>

<script>
export default {
    props:{
        newitem:Object,
        charas:Array,
        results:Array,
    }
}
</script>