<template>
    <v-container>
        <v-card outlined>
          <v-container>
        <v-simple-table fixed-header height="500px">
          <thead>
            <tr>
              <th class="text-left">日付</th>
              <th class="text-left">時間</th>
              <th class="text-left">勝敗</th>
              <th class="text-left">自キャラ</th>
              <th class="text-left">相手キャラ</th>
              <th class="text-left">編集・削除</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in memos" :key="item.name">
              <td><v-text-field v-model="item.date" type="date"></v-text-field></td>
              <td><v-text-field v-model="item.time" type="time"></v-text-field></td>
              <td><v-select
              v-model="item.result"
              :items="results"
              item-text="result" 
              item-value="id"
              ></v-select>
            </td>
              <td><v-select
              v-model="item.my_chara"
              :items="charas"
              item-text="character" 
              item-value="id"
            ></v-select></td>
              <td><v-select
              v-model="item.op_chara"
              :items="charas"
              item-text="character" 
              item-value="id"
            ></v-select></td>
              <td>
                <v-icon
                  v-model="item.id"
                  small
                  class="mr-2"
                  @click="$emit('editItem',{item})"   
                >
                  mdi-pencil
                </v-icon>
                <v-icon
                  v-model="item.id"
                  small
                  @click="$emit('deleteItem',{item})" 
                >
                  mdi-delete
                </v-icon>
              </td>
            </tr>
          </tbody>
        </v-simple-table>
        </v-container>
        </v-card>
    </v-container>
</template>

<script>
export default {
  props:{
    memos:Array,
    charas:Array,
    results:Array,}
    

}
</script>