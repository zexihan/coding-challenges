void mergeSort(vector<int> &a, vector<int> &T, int left, int right) {
    if (right - left == 1) 
        return;
    
    int mid = left + right >> 1;
    mergeSort(a, T, left, mid);
    mergeSort(a, T, mid, right);

    int tmid = left + right >> 1;
    int tleft = left;
    int i = left;

    while (tleft < mid || tmid < right) {
        if (tmid >= right || (tleft < mid && a[tleft <= a[tmid]]))
            T[i++] = a[tleft++];
        else
            T[i++] = a[tmid++];
    }
    for (int i = left; i < right; i++)
        a[i] = T[i];
}

void mSort(vector<int> &a) {
    int len = a.size();
    vector<int> T(len);
    mergeSort(a, T, 0, len);
}