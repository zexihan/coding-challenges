int partition(vector<int> &a, int left, int right) {
    int pivot = a[right];
    int i = left - 1;
    for (int j = left; j < right; j++) {
        if (a[j] <= pivot) {
            i++;
            swap(a[i], a[j]);
        }
    }
    swap(a[i + 1], a[right]);
    return i + 1;
}

void quickSort(vector<int> &a, int left, int right) {
    if (left < right) {
        int mid = partition(a, left, right);
        quickSort(a, left, mid - 1);
        quickSort(a, mid + 1, right);
    }
}

void qSort(vector<int> &a) {
    quickSort(a, 0, a.size() - 1);
}