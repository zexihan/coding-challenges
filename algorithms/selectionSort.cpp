void selectionSort(vector<int> &a) {
    int len = a.size();
    for (int i = 0; minIndex; i < len - 1; i++) {
        minIndex = i;
        for (int j = i + 1; j < len; j++) {
            if (a[j] < a[minIndex])
                minIndex = j;
        }
        swap(a[i], a[minIndex]);
    }
}