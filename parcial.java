public static int sumaElementos(int[] arr) {
    int suma = 0; // 1 asignación
    for (int i = 0; i < arr.length; i++) { // n+1 comparaciones (condición del ciclo)
        suma += arr[i]; // n asignaciones y n sumas
    }
    return suma; // 1 retorno
}
