def shifted_binary_search(lst, val):
    l_p = 0
    r_p = len(lst)
    while l_p < r_p:
        m_p = (l_p + r_p) // 2
        l_val, r_val, m_val = lst[l_p], lst[r_p], lst[m_p]


def find_pivot(lst):
    min_val = 100000000000
    min_index = -1
    l_p = 0
    r_p = len(lst)
    while l_p < r_p:
        m_p = (l_p + r_p) // 2
        m_val = lst[m_p]
        if min_val > m_val:
            min_val = m_val
            min_index = m_p
        if lst[l_p] > lst[r_p]:
            r_p = m_p + 1

    return None
