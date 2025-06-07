<?php

/*
 * Complete the 'migratoryBirds' function below.
 *
 * In the function 'migratoryBirds' determine(return) the id of the most frequently sighted type
 * if the maximum value occurs in more than one id return the smallest id
 * For example in array [1, 2, 2, 3, 3]; you should return 2
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY arr as parameter.
 */

function migratoryBirds($arr) {
    // Write your code here
    $ids_array = array();
    for ($i = 0; $i < sizeof($arr); $i++) {
        $ids_array[$arr[$i]] = 0;
    }

    for ($i = 0; $i < sizeof($arr); $i++) {
        if (array_key_exists($arr[$i], $ids_array)) {
            $ids_array[$arr[$i]] += 1;
        }
    }
    $max_count = max($ids_array);
    $most_ids = array_keys($ids_array, $max_count);
    print_r($most_ids);
    return min($most_ids);
}
?>
