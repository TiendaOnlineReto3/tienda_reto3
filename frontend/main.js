import axios from 'axios';

const app = Vue.createApp({
    data() {
        return {
            products: [
                // {
                //     id:1,
                //     nombre: 'Chaqueta corta',
                //     image: 'img/chaqueta1.avif',
                //     description: 'Chaqueta corta de hombre Lacoste acolchada e hidrófuga',
                //     price: 69.99,
                //     quantity: 1,
                //     category: 'Cazadora',
                // },
                // {
                //     id:2,
                //     nombre: 'Chaqueta de plumón',
                //     image: 'img/chaqueta2.avif',
                //     description: 'Packaway de tela con capucha y cremallera',
                //     price: 49.99,
                //     quantity: 1,
                //     category: 'Cazadora',
                // },
                // {
                //     id:3,
                //     nombre: 'Chaqueta Sport',
                //     image: 'img/chaqueta3.avif',
                //     description: 'Fabricado con fibra reciclada con capucha y cremallera',
                //     price: 49.99,
                //     quantity: 1,
                //     category: 'Cazadora',
                // },
                // {
                //     id:4,
                //     nombre: 'Chaqueta bomber',
                //     image: 'img/chaqueta4.avif',
                //     description: 'Lacoste en tafetán acolchado con diseño reversible',
                //     price: 49.99,
                //     quantity: 1,
                //     category: 'Cazadora',
                // },
                // {
                //     id:5,
                //     nombre: 'Chaqueta bomber',
                //     image: 'img/chaqueta5.avif',
                //     description: 'Lacoste en tafetán acolchado con diseño reversible',
                //     price: 49.99,
                //     quantity: 1,
                //     category: 'Cazadora',
                // },
                // {
                //     id:6,
                //     nombre: 'Camiseta1',
                //     image: 'img/camiseta1.avif',
                //     description: 'Lacoste en tafetán acolchado con diseño reversible',
                //     price: 49.99,
                //     quantity: 1,
                //     category: 'Camiseta',
                // },
                // {
                //     id:7,
                //     nombre: 'Camiseta2',
                //     image: 'img/camiseta2.avif',
                //     description: 'Lacoste en tafetán acolchado con diseño reversible',
                //     price: 49.99,
                //     quantity: 1,
                //     category: 'Camiseta',
                // },
                // {
                //     id:8,
                //     nombre: 'Camiseta3',
                //     image: 'img/camiseta3.avif',
                //     description: 'Lacoste en tafetán acolchado con diseño reversible',
                //     price: 49.99,
                //     quantity: 1,
                //     category: 'Camiseta',
                // },
                // {
                //     id:9,
                //     nombre: 'Camiseta4',
                //     image: 'img/camiseta4.avif',
                //     description: 'Lacoste en tafetán acolchado con diseño reversible',
                //     price: 49.99,
                //     quantity: 1,
                //     category: 'Camiseta',
                // },
                // {
                //     id:10,
                //     nombre: 'Camiseta5',
                //     image: 'img/camiseta5.avif',
                //     description: 'Lacoste en tafetán acolchado con diseño reversible',
                //     price: 49.99,
                //     quantity: 1,
                //     category: 'Camiseta',
                // },
                // {
                //     id:11,
                //     nombre: 'Pantalon1',
                //     image: 'img/pantalon1.avif',
                //     description: 'Lacoste en tafetán acolchado con diseño reversible',
                //     price: 49.99,
                //     quantity: 1,
                //     category: 'Pantalon',
                // },
                // {
                //     id:12,
                //     nombre: 'Pantalon2',
                //     image: 'img/pantalon2.avif',
                //     description: 'Lacoste en tafetán acolchado con diseño reversible',
                //     price: 49.99,
                //     quantity: 1,
                //     category: 'Pantalon',
                // },
                // {
                //     id:13,
                //     nombre: 'Pantalon3',
                //     image: 'img/pantalon3.avif',
                //     description: 'Lacoste en tafetán acolchado con diseño reversible',
                //     price: 49.99,
                //     quantity: 1,
                //     category: 'Pantalon',
                // },
                // {
                //     id:14,
                //     nombre: 'Pantalon4',
                //     image: 'img/pantalon4.avif',
                //     description: 'Lacoste en tafetán acolchado con diseño reversible',
                //     price: 49.99,
                //     quantity: 1,
                //     category: 'Pantalon',
                // },
                // {
                //     id:15,
                //     nombre: 'Pantalon5',
                //     image: 'img/pantalon5.avif',
                //     description: 'Lacoste en tafetán acolchado con diseño reversible',
                //     price: 49.99,
                //     quantity: 1,
                //     category: 'Pantalon',
                // },
                // {
                //     id:16,
                //     nombre: 'Sudadera1',
                //     image: 'img/sudadera1.avif',
                //     description: 'Lacoste en tafetán acolchado con diseño reversible',
                //     price: 49.99,
                //     quantity: 1,
                //     category: 'Sudadera',
                // },
                // {
                //     id:17,
                //     nombre: 'Sudadera2',
                //     image: 'img/sudadera2.avif',
                //     description: 'Lacoste en tafetán acolchado con diseño reversible',
                //     price: 49.99,
                //     quantity: 1,
                //     category: 'Sudadera',
                // },
                // {
                //     id:18,
                //     nombre: 'Sudadera3',
                //     image: 'img/sudadera3.avif',
                //     description: 'Lacoste en tafetán acolchado con diseño reversible',
                //     price: 49.99,
                //     quantity: 1,
                //     category: 'Sudadera',
                // },
                // {
                //     id:19,
                //     nombre: 'Sudadera4',
                //     image: 'img/sudadera4.avif',
                //     description: 'Lacoste en tafetán acolchado con diseño reversible',
                //     price: 49.99,
                //     quantity: 1,
                //     category: 'Sudadera',
                // },
                // {
                //     id:20,
                //     nombre: 'Sudadera5',
                //     image: 'img/sudadera5.avif',
                //     description: 'Lacoste en tafetán acolchado con diseño reversible',
                //     price: 49.99,
                //     quantity: 1,
                //     category: 'Sudadera',
                // },
                
            ],
            
            cart: [],
            isCartOpen: false,
            isUpdateIndicatorVisible: false,
            selectedCurrency: '', // Moneda por defecto
            selectedCategory: 'Todos', // Categoría por defecto
            favorites: [],
            isDragging: false,
            startX: 0,
            scrollLeft: 0,

        };
    },
    computed: {
        filteredCamisetas() {
            return this.products.filter(product => product.category === 'Camiseta');
        },
        filteredCazadoras() {
            return this.products.filter(product => product.category === 'Cazadora');
        },
        filteredPantalones() {
            return this.products.filter(product => product.category === 'Pantalon');
        },
        filteredSudaderas() {
            return this.products.filter(product => product.category === 'Sudadera');
        },
        filteredProducts() {
            if (this.selectedCategory === 'Todos') {
                return this.products;
            } else {
                return this.products.filter(product => product.category === this.selectedCategory);
            }
        },
    },
    methods: {
        // Método para cargar los productos desde la API
        async loadProducts() {
            try {
                const response = await axios.get('http://localhost:4000/articulo');
                // Asigna los productos obtenidos a la propiedad "products"
                this.products = response.data.articulos;
            } catch (error) {
                console.error('Error al cargar productos desde la API:', error);
            }
        },        
        decreaseQuantity(product) {
            if (product.quantity > 1) {
              product.quantity--;
            }
          },
          // Método para aumentar la cantidad
          increaseQuantity(product) {
            product.quantity++;
          },
          handleMouseDown(event) {
            this.isDragging = true;
            this.startX = event.pageX - this.$refs.cardRow.offsetLeft;
            this.scrollLeft = this.$refs.cardRow.scrollLeft;
          },
          handleMouseUp() {
            this.isDragging = false;
          },
          handleMouseMove(event) {
            if (!this.isDragging) return;
            const x = event.pageX - this.$refs.cardRow.offsetLeft;
            const walk = (x - this.startX) * 3; // Ajusta este valor según tus preferencias
            this.$refs.cardRow.scrollLeft = this.scrollLeft - walk;
          },
        addToCart(index, quantity) {
            const existingCartItemIndex = this.cart.findIndex(item => item.index === index);

            if (existingCartItemIndex !== -1) {
                // Si el producto ya está en el carrito, actualiza la cantidad
                this.cart[existingCartItemIndex].quantity += quantity;
            } else {
                // Si el producto no está en el carrito, agrégalo
                this.cart.push({ index, quantity });
            }

            // Mostrar el indicador de actualización
            this.isUpdateIndicatorVisible = true;
        },
        removeFromCart(index) {
            this.cart.splice(index, 1);
        },
        calculateTotal() {
            return this.cart.reduce((total, item) => total + this.products[item.index].price * item.quantity, 0);
        },
        toggleCart() {
            this.isCartOpen = !this.isCartOpen;
        },
        countTotalItemsInCart() {
            return this.cart.reduce((totalItems, item) => totalItems + item.quantity, 0);
        },
        // Método para actualizar la moneda seleccionada
        updateCurrency() {
            const apiKey = 'fca_live_1pwfsm4S40P2Q70dvJGfsmRYcwGF5eX0ukCk8cVG';
            const baseCurrency = 'USD';

            // Llamar a la API para obtener los tipos de cambio
            fetch(`https://freecurrencyapi.net/api/v2/latest?apikey=${apiKey}&base_currency=${baseCurrency}`)
                .then(response => response.json())
                .then(data => {
                    // Actualizar la moneda seleccionada
                    this.selectedCurrency = data.data.base_currency;

                    // Actualizar los precios de los productos según la moneda seleccionada
                    this.products.forEach(product => {
                        const originalPrice = product.price;
                        const exchangeRate = data.data.rates[this.selectedCurrency];
                        product.price = originalPrice * exchangeRate;
                    });
                })
                .catch(error => console.error('Error al obtener tipos de cambio:', error));
        },
        formatPrice(price) {
            return `$${price.toFixed(2)}`;
        },
        filterByCategory(category) {
            this.selectedCategory = category;
        },
        addToFavorites(index) {
            // Agrega el producto al array de favoritos
            this.favorites.push(this.filteredProducts[index]);
          },
          removeFromFavorites(index) {
            // Remueve el producto del array de favoritos
            this.favorites.splice(index, 1);
          },
          isFavorite(index) {
            // Verifica si el producto está en la lista de favoritos
            return this.favorites.includes(this.filteredProducts[index]);
          }
    },
    watch: {
        // Observador para la moneda seleccionada
        selectedCurrency: 'updateCurrency',
    },
    mounted() {
        // Inicialmente, actualizar la moneda al cargar la página
        this.updateCurrency();
         // Llama a la función para cargar productos cuando el componente está montado
         this.loadProducts();
         // Inicialmente, actualizar la moneda al cargar la página
         this.updateCurrency();
     },
    },

);



app.mount('#app');