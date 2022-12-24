from typing import Literal

from mipac.exception import InvalidParamError, NoSuchNoteError, NoSuchUserError

EXCEPTION_ID_MAP = {
    InvalidParamError: ['3d81ceae-475f-4600-b2a8-2bc116157532'],
    NoSuchNoteError: [
        'ee449fbe-af2a-453b-9cae-cf2fe7c895fc',
        'fc8c0b49-c7a3-4664-a0a6-b418d386bb8b',
        'aff017de-190e-434b-893e-33a9ff5049d8',
        '56734f8b-3928-431e-bf80-6ff87df40cb3',
        '454170ce-9d63-4a43-9da1-ea10afe81e21',
        '24fcbfc6-2e37-42b6-8388-c29b3861a08d',
        '47db1a1c-b0af-458d-8fb4-986e4efafe1e',
        'e1035875-9551-45ec-afa8-1ded1fcb53c8',
        '490be23f-8c1f-4796-819f-94cb4f9d1630',
        '263fff3d-d0e1-4af4-bea7-8408059b451a',
        '12908022-2e21-46cd-ba6a-3edaf6093f46',
        'bea9b03f-36e0-49c5-a4db-627a029f8971',
        'efd4a259-2442-496b-8dd7-b255aa1a160f',
        '6dd26674-e060-4816-909a-45ba3f4da458',
        '80848a2c-398f-4343-baa9-df1d57696c56',
        'ecafbd2e-c283-4d6d-aecb-1a0a33b75396',
        '033d0620-5bfe-4027-965d-980b0c85a3ea',
        '764d9fce-f9f2-4a0e-92b1-6ceac9a7ad37',
        '5ff67ada-ed3b-2e71-8e87-a1a421e177d2',
        'bddd57ac-ceb3-b29d-4334-86ea5fae481a',
        'd785b897-fcd3-4fe9-8fc3-b85c26e6c932',
        'fcd2eef9-a9b2-4c4f-8624-038099e90aa5',
    ],
    NoSuchUserError: [
        '4362f8dc-731f-4ad8-a694-be5a88922a24',
        '27e494ba-2ac2-48e8-893b-10d4d8c2387b',
        '7cc4f851-e2f1-4621-9633-ec9e1d00c01e',
        '8621d8bf-c358-4303-a066-5ea78610eb3f',
        '5b12c78d-2b28-4dca-99d2-f56139b42ff8',
        '66ce1645-d66c-46bb-8b79-96739af885bd',
        '4e68c551-fc4c-4e46-bb41-7d4a37bf9dab',
        'abc2ffa6-25b2-4380-ba99-321ff3a94555',
        '11795c64-40ea-4198-b06e-3c873ed9039d',
        '6fef56f3-e765-4957-88e5-c6f65329b8a5',
        'b851d00b-8ab1-4a56-8b1b-e24187cb48ef',
        '27fa5435-88ab-43de-9360-387de88727cd',
        '63e4aba4-4156-4e53-be25-c9559e42d71b',
        'e6965129-7b2a-40a4-bae2-cd84cd434822',
        '1acefcb5-0959-43fd-9685-b48305736cb5',
        '9e638e45-3b25-4ef7-8f95-07e8498f1819',
        'da52de61-002c-475b-90e1-ba64f9cf13a8',
        '0b5cc374-3681-41da-861e-8bc1146f7a55',
        '711f7ebb-bbb9-4dfa-b540-b27809fed5e9',
        '588e7f72-c744-4a61-b180-d354e912bda2',
        'a89abd3d-f0bc-4cce-beb1-2f446f4f1e6a',
    ],
}
ENDPOINTS = Literal[
    '/api/admin/abuse-user-reports',
    '/api/admin/accounts/create',
    '/api/admin/accounts/delete',
    '/api/admin/ad/create',
    '/api/admin/ad/delete',
    '/api/admin/ad/list',
    '/api/admin/ad/update',
    '/api/admin/announcements/create',
    '/api/admin/announcements/delete',
    '/api/admin/announcements/list',
    '/api/admin/announcements/update',
    '/api/admin/delete-account',
    '/api/admin/delete-all-files-of-a-user',
    '/api/admin/delete-logs',
    '/api/admin/drive-capacity-override',
    '/api/admin/drive/clean-remote-files',
    '/api/admin/drive/cleanup',
    '/api/admin/drive/files',
    '/api/admin/drive/show-file',
    '/api/admin/emoji/add',
    '/api/admin/emoji/add-aliases-bulk',
    '/api/admin/emoji/copy',
    '/api/admin/emoji/delete',
    '/api/admin/emoji/delete-bulk',
    '/api/admin/emoji/list',
    '/api/admin/emoji/list-remote',
    '/api/admin/emoji/remove',
    '/api/admin/emoji/remove-aliases-bulk',
    '/api/admin/emoji/set-aliases-bulk',
    '/api/admin/emoji/set-category-bulk',
    '/api/admin/emoji/update',
    '/api/admin/federation/delete-all-files',
    '/api/admin/federation/refresh-remote-instance-metadata',
    '/api/admin/federation/remove-all-following',
    '/api/admin/federation/update-instance',
    '/api/admin/get-index-stats',
    '/api/admin/get-table-stats',
    '/api/admin/get-user-ips',
    '/api/admin/invite',
    '/api/admin/logs',
    '/api/admin/meta',
    '/api/admin/moderators/add',
    '/api/admin/moderators/remove',
    '/api/admin/promo/create',
    '/api/admin/queue/clear',
    '/api/admin/queue/deliver-delayed',
    '/api/admin/queue/inbox-delayed',
    '/api/admin/queue/jobs',
    '/api/admin/queue/stats',
    '/api/admin/relays/add',
    '/api/admin/relays/list',
    '/api/admin/relays/remove',
    '/api/admin/remove-abuse-user-report',
    '/api/admin/reset-password',
    '/api/admin/resolve-abuse-user-report',
    '/api/admin/resync-chart',
    '/api/admin/send-email',
    '/api/admin/server-info',
    '/api/admin/set-premium',
    '/api/admin/show-moderation-logs',
    '/api/admin/show-user',
    '/api/admin/show-users',
    '/api/admin/silence-user',
    '/api/admin/suspend-user',
    '/api/admin/unset-premium',
    '/api/admin/unsilence-user',
    '/api/admin/unsuspend-user',
    '/api/admin/unverify-user',
    '/api/admin/update-meta',
    '/api/admin/update-remote-user',
    '/api/admin/update-user-note',
    '/api/admin/vacuum',
    '/api/admin/verify-user',
    '/api/announcements',
    '/api/antennas/create',
    '/api/antennas/delete',
    '/api/antennas/list',
    '/api/antennas/notes',
    '/api/antennas/show',
    '/api/antennas/update',
    '/api/ap/get',
    '/api/ap/show',
    '/api/app/create',
    '/api/app/show',
    '/api/auth/session/generate',
    '/api/auth/session/show',
    '/api/auth/session/userkey',
    '/api/blocking/create',
    '/api/blocking/delete',
    '/api/blocking/list',
    '/api/channels/create',
    '/api/channels/featured',
    '/api/channels/follow',
    '/api/channels/followed',
    '/api/channels/owned',
    '/api/channels/pin-note',
    '/api/channels/show',
    '/api/channels/timeline',
    '/api/channels/unfollow',
    '/api/channels/update',
    '/api/charts/active-users',
    '/api/charts/ap-request',
    '/api/charts/drive',
    '/api/charts/federation',
    '/api/charts/hashtag',
    '/api/charts/instance',
    '/api/charts/network',
    '/api/charts/notes',
    '/api/charts/user/drive',
    '/api/charts/user/following',
    '/api/charts/user/notes',
    '/api/charts/user/reactions',
    '/api/charts/users',
    '/api/clips/add-note',
    '/api/clips/create',
    '/api/clips/delete',
    '/api/clips/list',
    '/api/clips/notes',
    '/api/clips/remove-note',
    '/api/clips/show',
    '/api/clips/update',
    '/api/drive',
    '/api/drive/files',
    '/api/drive/files/attached-notes',
    '/api/drive/files/check-existence',
    '/api/drive/files/create',
    '/api/drive/files/delete',
    '/api/drive/files/find',
    '/api/drive/files/find-by-hash',
    '/api/drive/files/show',
    '/api/drive/files/update',
    '/api/drive/files/upload-from-url',
    '/api/drive/folders',
    '/api/drive/folders/create',
    '/api/drive/folders/delete',
    '/api/drive/folders/find',
    '/api/drive/folders/show',
    '/api/drive/folders/update',
    '/api/drive/stream',
    '/api/email-address/available',
    '/api/endpoint',
    '/api/endpoints',
    '/api/federation/followers',
    '/api/federation/following',
    '/api/federation/instances',
    '/api/federation/show-instance',
    '/api/federation/stats',
    '/api/federation/update-remote-user',
    '/api/federation/users',
    '/api/fetch-rss',
    '/api/following/create',
    '/api/following/delete',
    '/api/following/invalidate',
    '/api/following/requests/accept',
    '/api/following/requests/cancel',
    '/api/following/requests/list',
    '/api/following/requests/reject',
    '/api/gallery/featured',
    '/api/gallery/popular',
    '/api/gallery/posts',
    '/api/gallery/posts/create',
    '/api/gallery/posts/delete',
    '/api/gallery/posts/like',
    '/api/gallery/posts/show',
    '/api/gallery/posts/unlike',
    '/api/gallery/posts/update',
    '/api/games/reversi/games',
    '/api/games/reversi/games/show',
    '/api/games/reversi/games/surrender',
    '/api/games/reversi/invitations',
    '/api/games/reversi/match',
    '/api/games/reversi/match/cancel',
    '/api/get-online-users-count',
    '/api/hashtags/list',
    '/api/hashtags/search',
    '/api/hashtags/show',
    '/api/hashtags/trend',
    '/api/hashtags/users',
    '/api/i',
    '/api/i/favorites',
    '/api/i/gallery/likes',
    '/api/i/gallery/posts',
    '/api/i/get-word-muted-notes-count',
    '/api/i/notifications',
    '/api/i/page-likes',
    '/api/i/pages',
    '/api/i/pin',
    '/api/i/read-all-messaging-messages',
    '/api/i/read-all-unread-notes',
    '/api/i/read-announcement',
    '/api/i/registry/get',
    '/api/i/registry/get-all',
    '/api/i/registry/get-detail',
    '/api/i/registry/keys',
    '/api/i/registry/keys-with-type',
    '/api/i/registry/remove',
    '/api/i/registry/scopes',
    '/api/i/registry/set',
    '/api/i/unpin',
    '/api/i/update',
    '/api/i/user-group-invites',
    '/api/i/webhooks/create',
    '/api/i/webhooks/delete',
    '/api/i/webhooks/list',
    '/api/i/webhooks/show',
    '/api/i/webhooks/update',
    '/api/messaging/history',
    '/api/messaging/messages',
    '/api/messaging/messages/create',
    '/api/messaging/messages/delete',
    '/api/messaging/messages/read',
    '/api/meta',
    '/api/mute/create',
    '/api/mute/delete',
    '/api/mute/list',
    '/api/my/apps',
    '/api/notes',
    '/api/notes/children',
    '/api/notes/clips',
    '/api/notes/conversation',
    '/api/notes/create',
    '/api/notes/delete',
    '/api/notes/favorites/create',
    '/api/notes/favorites/delete',
    '/api/notes/featured',
    '/api/notes/global-timeline',
    '/api/notes/hybrid-timeline',
    '/api/notes/local-timeline',
    '/api/notes/mentions',
    '/api/notes/polls/recommendation',
    '/api/notes/polls/vote',
    '/api/notes/reactions',
    '/api/notes/reactions/create',
    '/api/notes/reactions/delete',
    '/api/notes/renotes',
    '/api/notes/replies',
    '/api/notes/search',
    '/api/notes/search-by-tag',
    '/api/notes/show',
    '/api/notes/state',
    '/api/notes/thread-muting/create',
    '/api/notes/thread-muting/delete',
    '/api/notes/timeline',
    '/api/notes/translate',
    '/api/notes/unrenote',
    '/api/notes/user-list-timeline',
    '/api/notes/watching/create',
    '/api/notes/watching/delete',
    '/api/notifications/create',
    '/api/notifications/mark-all-as-read',
    '/api/notifications/read',
    '/api/pages/create',
    '/api/pages/delete',
    '/api/pages/featured',
    '/api/pages/like',
    '/api/pages/show',
    '/api/pages/unlike',
    '/api/pages/update',
    '/api/ping',
    '/api/pinned-users',
    '/api/promo/read',
    '/api/request-reset-password',
    '/api/reset-db',
    '/api/reset-password',
    '/api/room/show',
    '/api/room/update',
    '/api/server-info',
    '/api/stats',
    '/api/sw/register',
    '/api/sw/unregister',
    '/api/test',
    '/api/username/available',
    '/api/users',
    '/api/users/clips',
    '/api/users/followers',
    '/api/users/following',
    '/api/users/gallery/posts',
    '/api/users/get-frequently-replied-users',
    '/api/users/groups/create',
    '/api/users/groups/delete',
    '/api/users/groups/invitations/accept',
    '/api/users/groups/invitations/reject',
    '/api/users/groups/invite',
    '/api/users/groups/joined',
    '/api/users/groups/leave',
    '/api/users/groups/owned',
    '/api/users/groups/pull',
    '/api/users/groups/show',
    '/api/users/groups/transfer',
    '/api/users/groups/update',
    '/api/users/lists/create',
    '/api/users/lists/delete',
    '/api/users/lists/list',
    '/api/users/lists/pull',
    '/api/users/lists/push',
    '/api/users/lists/show',
    '/api/users/lists/update',
    '/api/users/notes',
    '/api/users/pages',
    '/api/users/reactions',
    '/api/users/recommendation',
    '/api/users/relation',
    '/api/users/report-abuse',
    '/api/users/search',
    '/api/users/search-by-username-and-host',
    '/api/users/show',
    '/api/users/stats',
    '/api/version',
]
