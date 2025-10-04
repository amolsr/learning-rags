// https://practice.geeksforgeeks.org/problems/kadanes-algorithm/0

/**
 * Given an array arr of N integers. Find the contiguous sub-array with maximum sum.
*/

#include <bits/stdc++.h>
#define ll long long
using namespace std;
int main()
{
    ll t;
    cin >> t;
    while (t--)
    {
        ll n;
        cin >> n;
        ll arr[n];
        for (ll i = 0; i < n; i++)
        {
            cin >> arr[i];
        }
        // making a greedy index prefix array
        // means the lower value will be added to higher index
        // only if its denotes the profit to that index (HIGHer)
        for (ll i = 1; i < n; i++)
        {
            ll temp = arr[i] + arr[i - 1];
            if (temp > arr[i])
            {
                arr[i] = temp;
            }
        }
        // finding the max from it
        ll result = LLONG_MIN;
        for (ll i = 0; i < n; i++)
        {
            if (arr[i] > result)
                result = arr[i];
        }
        cout << result << "\n";
    }
}