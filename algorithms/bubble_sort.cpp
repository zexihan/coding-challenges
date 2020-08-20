void bubbleSort(vector<int> &a) {
    int len = a.size();
    for (int i = 0; i < len - 1; i++) {
        for (int j = 0; j < len - 1 - i; j++) {
            if (a[j] > a[j + 1]) {
                swap(a[j], a[j+1]);
            }
        }
    }
}