// Last updated: 8/16/2026, 9:49:05 PM
class TimeMap {
    Map<String, List<Pair>> timeMap;
    public TimeMap() {
        timeMap = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        List<Pair> valList = timeMap.getOrDefault(key, new ArrayList<>());
        valList.add(new Pair(timestamp, value));
        timeMap.put(key, valList);
    }
    
    // All the timestamps timestamp of set are strictly increasing.
    // means its already sorted by ts after adding
    // O(logn) to find last one <= timestamp.
    public String get(String key, int timestamp) {
        if (!timeMap.containsKey(key)) return "";
        List<Pair> valList = timeMap.get(key);

        int n = valList.size();
        int l = 0, r = n - 1;
        while (l + 1 < r) {
            int mid = l + (r - l) / 2;
            Pair curr = valList.get(mid);
            if (curr.ts == timestamp) return curr.val;
            if (curr.ts < timestamp) l = mid;
            if (curr.ts > timestamp) r = mid;
        }
        // check r first, cause we are finding last one <= timestamp
        if (valList.get(r).ts <= timestamp) return valList.get(r).val;
        if (valList.get(l).ts <= timestamp) return valList.get(l).val;
        return "";
    }
}

class Pair {
    int ts;
    String val;
    Pair(int ts, String val) {
        this.ts = ts;
        this.val = val;
    }
}
/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */