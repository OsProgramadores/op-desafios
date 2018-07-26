// namespace desafio5
// {
//     public class List<T>
//     {

//         ListItem<T> itens;
//         ListItem<T> last;

//         public List(T item)
//         {
//             this.itens = new ListItem<T>(item);
            
//             last = this.itens;
//         }

//         public void Add(T item)
//         {
//             last.next = new ListItem<T>(item);
//         }




//         private class ListItem<T>
//         {
//             public T current;
//             public ListItem<T> next;

//             public ListItem(T item)
//             {
//                 this.current = item;
//             }
//         }
//     }


// }