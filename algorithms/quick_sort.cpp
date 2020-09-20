int partition(vector<int> &a, int left, int right) {
    int random = rand() % (right - left + 1) + left;
    swap(a[random], a[left]);
    int pivot = a[left];
    
    int lo = left;
    int cur = left + 1;
    while (cur <= right) {
        if (a[cur] <= pivot) {
            swap(a[lo + 1], a[cur]);
            lo++;
        }
        cur++;
    }
    swap(a[lo], a[left]);
    return lo;
}

void quickSort(vector<int> &a, int left, int right) {
    if (left < right) {
        int p = partition(a, left, right);
        quickSort(a, left, p - 1);
        quickSort(a, p + 1, right);
    }
}

void qSort(vector<int> &a) {
    quickSort(a, 0, a.size() - 1);
}