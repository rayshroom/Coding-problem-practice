/*

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
*/

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* swapNodes(ListNode* head, int k) {
        ListNode* rtn = head;
        ListNode* itr = head;
        ListNode* itr2 = head;
        vector<int> cnt;
        while (itr != nullptr) {
            cnt.push_back(itr->val);
            itr = itr->next;
        }
        
        int tmp = cnt[cnt.size() - k];
        cnt[cnt.size() - k] = cnt[k - 1];
        cnt[k - 1] = tmp;
        
        int i = 0;
        while (itr2 != nullptr) {
            if (itr2->val != cnt[i]) {
                itr2->val = cnt[i];
            }
            itr2 = itr2->next;
            i++;
        }
        
        return rtn;
    }
};