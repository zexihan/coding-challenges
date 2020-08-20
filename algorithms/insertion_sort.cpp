void insertionSort(vector<int> &a) {
    int len = a.size();
    for (int i = 0; j, temp; i < len - 1; i++) {
        j = i;
        temp = a[i + 1];
        while (j >= 0 && a[j] > temp) {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = temp;
    }
}