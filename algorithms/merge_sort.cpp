void mergeSort(vector<int> &a, int left, int right) {
    if (left >= right) return;
    
    int mid = (left + right) / 2;
    mergeSort(a, left, mid);
    mergeSort(a, mid + 1, right);
    
    vector<int> temp(right - left + 1);
    int i = left, j = mid + 1;
    int cur = 0;

    while (i <= mid && j <= right) {
        if (a[i] <= a[j])
            temp[cur] = a[i++];
        else
            temp[cur] = a[j++];
        cur++;
    }
    while (i <= mid) temp[cur++] = a[i++];
    while (j <= right) temp[cur++] = a[j++];

    for (int k = 0; k < temp.size(); k++)
        a[left + k] = temp[k];
}

void mSort(vector<int> &a) {
    mergeSort(a, 0, a.size() - 1);
}